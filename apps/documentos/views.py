from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import Documento
from .forms import DocumentoForm


class DocumentosListView(TemplateView):
    template_name = "documentos/lista.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["documentos"] = Documento.objects.select_related("cliente", "categoria", "estado").order_by("-fecha")
        return context


class DocumentoNuevoView(TemplateView):
    template_name = "documentos/nuevo.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = DocumentoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.subido_por = request.user
            documento.save()
            return redirect("documentos-lista")

        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = form
        return self.render_to_response(context)


class DocumentoEditarView(TemplateView):
    template_name = "documentos/editar.html"

    def get_context_data(self, **kwargs):
        documento = get_object_or_404(Documento, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = DocumentoForm(instance=documento)
        context["documento"] = documento
        return context

    def post(self, request, *args, **kwargs):
        documento = get_object_or_404(Documento, pk=kwargs["pk"])
        form = DocumentoForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            doc_editado = form.save(commit=False)
            doc_editado.subido_por = documento.subido_por
            doc_editado.version += 1  # cada edición sube la versión
            doc_editado.save()
            return redirect("documentos-lista")

        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = form
        context["documento"] = documento
        return self.render_to_response(context)


class DocumentoEliminarView(TemplateView):
    template_name = "documentos/eliminar.html"

    def get_context_data(self, **kwargs):
        documento = get_object_or_404(Documento, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["documento"] = documento
        return context

    def post(self, request, *args, **kwargs):
        documento = get_object_or_404(Documento, pk=kwargs["pk"])
        documento.delete()
        return redirect("documentos-lista")


# class DocumentoDetalleView(TemplateView):
#     template_name = "documentos/detalle.html"
#
#     def get_context_data(self, **kwargs):
#         documento = get_object_or_404(Documento, pk=kwargs["pk"])
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["documento"] = documento
#         return context


class DocumentoDetalleView(TemplateView):
    template_name = "documentos/detalle.html"

    def get_context_data(self, **kwargs):
        documento = get_object_or_404(Documento, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["documento"] = documento
        # 👇 añadimos la URL absoluta del archivo para usarla en el iframe del visor Word/Excel
        context["archivo_absoluto"] = self.request.build_absolute_uri(documento.archivo.url)
        return context


