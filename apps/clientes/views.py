from django.shortcuts import render

# # Create your views here.
# from django.views.generic import TemplateView
# from web_project import TemplateLayout
# from .models import Cliente
# from django.shortcuts import redirect
# from django.views.generic import TemplateView
# from web_project import TemplateLayout
# from .models import Cliente, TipoCliente
# class ClientesListView(TemplateView):
#     template_name = "clientes/lista.html"
#
#     def get_context_data(self, **kwargs):
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["clientes"] = Cliente.objects.all()
#         return context
#
#
# class ClienteNuevoView(TemplateView):
#     template_name = "clientes/nuevo.html"
#
#     def get_context_data(self, **kwargs):
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["tipos_clientes"] = TipoCliente.objects.all()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         nombre = request.POST.get("nombre")
#         correo = request.POST.get("correo")
#         telefono = request.POST.get("telefono")
#         nit = request.POST.get("nit")
#         direccion = request.POST.get("direccion")
#         tipo_cliente_id = request.POST.get("tipo_cliente")
#
#         if tipo_cliente_id:
#             tipo_cliente = TipoCliente.objects.get(id=tipo_cliente_id)
#         else:
#             tipo_cliente = None
#
#         Cliente.objects.create(
#             nombre=nombre,
#             correo=correo,
#             telefono=telefono,
#             nit=nit,
#             direccion=direccion,
#             tipo_cliente=tipo_cliente
#         )
#
#         return redirect("clientes-lista")
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import Cliente, TipoCliente


class ClientesListView(TemplateView):
    template_name = "clientes/lista.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["clientes"] = Cliente.objects.all()
        return context


class ClienteNuevoView(TemplateView):
    template_name = "clientes/nuevo.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["tipos_clientes"] = TipoCliente.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        telefono = request.POST.get("telefono")
        nit = request.POST.get("nit")
        direccion = request.POST.get("direccion")
        tipo_cliente_id = request.POST.get("tipo_cliente")
        tipo_contribuyente = request.POST.get("tipo_contribuyente")

        tipo_cliente = TipoCliente.objects.filter(id=tipo_cliente_id).first()

        Cliente.objects.create(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            nit=nit,
            direccion=direccion,
            tipo_cliente=tipo_cliente,
            tipo_contribuyente=tipo_contribuyente
        )
        return redirect("clientes-lista")


class ClienteEditarView(TemplateView):
    template_name = "clientes/editar.html"

    def get_context_data(self, **kwargs):
        cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["cliente"] = cliente
        context["tipos_clientes"] = TipoCliente.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        cliente = get_object_or_404(Cliente, pk=kwargs["pk"])

        cliente.nombre = request.POST.get("nombre")
        cliente.correo = request.POST.get("correo")
        cliente.telefono = request.POST.get("telefono")
        cliente.nit = request.POST.get("nit")
        cliente.direccion = request.POST.get("direccion")
        cliente.tipo_contribuyente = request.POST.get("tipo_contribuyente")

        tipo_cliente_id = request.POST.get("tipo_cliente")
        cliente.tipo_cliente = TipoCliente.objects.filter(id=tipo_cliente_id).first()

        cliente.save()
        return redirect("clientes-lista")


class ClienteEliminarView(TemplateView):
    template_name = "clientes/eliminar.html"

    def get_context_data(self, **kwargs):
        cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["cliente"] = cliente
        return context

    def post(self, request, *args, **kwargs):
        cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
        cliente.delete()
        return redirect("clientes-lista")


class ClienteDetalleView(TemplateView):
    template_name = "clientes/detalle.html"

    def get_context_data(self, **kwargs):
        cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["cliente"] = cliente

        # Documentos según tipo de contribuyente
        if cliente.tipo_contribuyente == "PEQUEÑO":
            context["documentos_requeridos"] = ["Facturas de ventas"]
        else:
            context["documentos_requeridos"] = [
                "Facturas de ventas",
                "Facturas de compras",
                "Estados de cuenta bancarios",
                "Planillas del IGSS",
                "Nómina de salarios",
                "Comprobantes de cheques y transferencias",
                "Otros comprobantes de pago"
            ]
        return context











# from django.shortcuts import redirect, get_object_or_404
# from django.views.generic import TemplateView
# from web_project import TemplateLayout
# from .models import Cliente, TipoCliente
#
#
# class ClientesListView(TemplateView):
#     template_name = "clientes/lista.html"
#
#     def get_context_data(self, **kwargs):
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["clientes"] = Cliente.objects.all()
#         return context
#
#
# class ClienteNuevoView(TemplateView):
#     template_name = "clientes/nuevo.html"
#
#     def get_context_data(self, **kwargs):
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["tipos_clientes"] = TipoCliente.objects.all()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         nombre = request.POST.get("nombre")
#         correo = request.POST.get("correo")
#         telefono = request.POST.get("telefono")
#         nit = request.POST.get("nit")
#         direccion = request.POST.get("direccion")
#         tipo_cliente_id = request.POST.get("tipo_cliente")
#
#         tipo_cliente = TipoCliente.objects.filter(id=tipo_cliente_id).first()
#
#         Cliente.objects.create(
#             nombre=nombre,
#             correo=correo,
#             telefono=telefono,
#             nit=nit,
#             direccion=direccion,
#             tipo_cliente=tipo_cliente
#         )
#         return redirect("clientes-lista")
#
#
# class ClienteEditarView(TemplateView):
#     template_name = "clientes/editar.html"
#
#     def get_context_data(self, **kwargs):
#         cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["cliente"] = cliente
#         context["tipos_clientes"] = TipoCliente.objects.all()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
#
#         cliente.nombre = request.POST.get("nombre")
#         cliente.correo = request.POST.get("correo")
#         cliente.telefono = request.POST.get("telefono")
#         cliente.nit = request.POST.get("nit")
#         cliente.direccion = request.POST.get("direccion")
#
#         tipo_cliente_id = request.POST.get("tipo_cliente")
#         cliente.tipo_cliente = TipoCliente.objects.filter(id=tipo_cliente_id).first()
#
#         cliente.save()
#         return redirect("clientes-lista")
#
#
# class ClienteEliminarView(TemplateView):
#     template_name = "clientes/eliminar.html"
#
#     def get_context_data(self, **kwargs):
#         cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["cliente"] = cliente
#         return context
#
#     def post(self, request, *args, **kwargs):
#         cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
#         cliente.delete()
#         return redirect("clientes-lista")
#
# class ClienteDetalleView(TemplateView):
#     template_name = "clientes/detalle.html"
#
#     def get_context_data(self, **kwargs):
#         cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["cliente"] = cliente
#
#         # Documentos requeridos según tipo
#         if cliente.tipo_contribuyente == "PEQUEÑO":
#             context["documentos_requeridos"] = [
#                 "Facturas de ventas"
#             ]
#         else:
#             context["documentos_requeridos"] = [
#                 "Facturas de ventas",
#                 "Facturas de compras",
#                 "Estados de cuenta bancarios",
#                 "Planillas del IGSS",
#                 "Nómina de salarios",
#                 "Comprobantes de cheques y transferencias",
#                 "Otros comprobantes de pago"
#             ]
#
#         return context

# class ClienteDetalleView(TemplateView):
#     template_name = "clientes/detalle.html"
#
#     def get_context_data(self, **kwargs):
#         cliente = get_object_or_404(Cliente, pk=kwargs["pk"])
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context["cliente"] = cliente
#         return context
