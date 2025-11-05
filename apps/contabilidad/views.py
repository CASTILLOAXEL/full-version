from django.shortcuts import render

# Create your views here.
# apps/contabilidad/views.py
import io
from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from web_project import TemplateLayout

# 📦 Librerías para exportar
from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

# 📚 Modelos y formularios
from .models import MovimientoContable
from .forms import MovimientoForm
from apps.clientes.models import Cliente  # ✅ Paso 3 — importar modelo Cliente


# ---------------------------------------------------------
# 📋 LISTADO DE MOVIMIENTOS
# ---------------------------------------------------------
class MovimientosListView(TemplateView):
    template_name = "contabilidad/lista.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["movimientos"] = MovimientoContable.objects.all().order_by('-fecha')
        return context


# ---------------------------------------------------------
# 📝 CREAR NUEVO MOVIMIENTO MANUAL
# ---------------------------------------------------------
class MovimientoNuevoView(TemplateView):
    template_name = "contabilidad/form.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = MovimientoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = MovimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contabilidad-lista")

        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = form
        return self.render_to_response(context)


# ---------------------------------------------------------
# 📊 VISTA DE REPORTES CONTABLES (GRÁFICOS Y BALANCES)
# ---------------------------------------------------------
class ReporteContableView(TemplateView):
    template_name = "contabilidad/reportes.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # 🔍 Filtros
        fecha_inicio = self.request.GET.get("inicio")
        fecha_fin = self.request.GET.get("fin")
        cliente_id = self.request.GET.get("cliente")

        movimientos = MovimientoContable.objects.all().order_by("-fecha")

        if fecha_inicio and fecha_fin:
            movimientos = movimientos.filter(fecha__range=[fecha_inicio, fecha_fin])
        if cliente_id:
            movimientos = movimientos.filter(cliente_id=cliente_id)

        # Totales
        total_ingresos = movimientos.filter(tipo="Ingreso").aggregate(Sum("monto"))["monto__sum"] or 0
        total_egresos = movimientos.filter(tipo="Egreso").aggregate(Sum("monto"))["monto__sum"] or 0
        balance = total_ingresos - total_egresos

        # Datos para gráfico
        data_ingresos = movimientos.filter(tipo="Ingreso").values_list("fecha", "monto")
        data_egresos = movimientos.filter(tipo="Egreso").values_list("fecha", "monto")

        context.update({
            "clientes": Cliente.objects.all(),  # ✅ Lista de clientes para el filtro
            "movimientos": movimientos,
            "total_ingresos": total_ingresos,
            "total_egresos": total_egresos,
            "balance": balance,
            "data_ingresos": list(data_ingresos),
            "data_egresos": list(data_egresos),
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
        })

        return context


# ---------------------------------------------------------
# 📤 EXPORTAR A EXCEL
# ---------------------------------------------------------
def exportar_excel(request):
    fecha_inicio = request.GET.get("inicio")
    fecha_fin = request.GET.get("fin")
    cliente_id = request.GET.get("cliente")

    movimientos = MovimientoContable.objects.all().order_by('-fecha')

    if fecha_inicio and fecha_fin:
        movimientos = movimientos.filter(fecha__range=[fecha_inicio, fecha_fin])
    if cliente_id:
        movimientos = movimientos.filter(cliente_id=cliente_id)

    wb = Workbook()
    ws = wb.active
    ws.title = "Movimientos Contables"

    # Encabezados
    ws.append(["Cliente", "Tipo", "Monto", "Fecha", "Descripción"])

    for m in movimientos:
        ws.append([
            m.cliente.nombre,
            m.tipo,
            float(m.monto),
            m.fecha.strftime("%d/%m/%Y"),
            m.descripcion or "-"
        ])

    # Estilo de encabezado
    for cell in ws[1]:
        cell.font = cell.font.copy(bold=True)
        cell.fill = cell.fill.copy(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

    # Respuesta HTTP
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="reporte_contable_{datetime.now().strftime("%Y%m%d")}.xlsx"'
    wb.save(response)
    return response


# ---------------------------------------------------------
# 📕 EXPORTAR A PDF
# ---------------------------------------------------------
def exportar_pdf(request):
    fecha_inicio = request.GET.get("inicio")
    fecha_fin = request.GET.get("fin")
    cliente_id = request.GET.get("cliente")

    movimientos = MovimientoContable.objects.all().order_by('-fecha')

    if fecha_inicio and fecha_fin:
        movimientos = movimientos.filter(fecha__range=[fecha_inicio, fecha_fin])
    if cliente_id:
        movimientos = movimientos.filter(cliente_id=cliente_id)

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("📊 Reporte de Movimientos Contables", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 20))

    # Tabla con los datos
    data = [["Cliente", "Tipo", "Monto (Q)", "Fecha", "Descripción"]]
    for m in movimientos:
        data.append([
            m.cliente.nombre,
            m.tipo,
            f"{m.monto:.2f}",
            m.fecha.strftime("%d/%m/%Y"),
            m.descripcion or "-"
        ])

    table = Table(data, colWidths=[100, 70, 70, 70, 160])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),
    ]))

    elements.append(table)
    doc.build(elements)

    buffer.seek(0)
    filename = f"reporte_contable_{datetime.now().strftime('%Y%m%d')}.pdf"
    return FileResponse(buffer, as_attachment=True, filename=filename)
