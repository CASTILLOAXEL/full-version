from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import EstadoDocumento


class EstadoListView(TemplateView):
    template_name = "estados/lista.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["estados"] = EstadoDocumento.objects.all().order_by("nombre")
        return context


class EstadoNuevoView(TemplateView):
    template_name = "estados/nueva.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get("nombre")
        color = request.POST.get("color") or "#000000"
        if nombre:
            EstadoDocumento.objects.create(nombre=nombre, color=color)
        return redirect("estados-lista")


class EstadoEditarView(TemplateView):
    template_name = "estados/editar.html"

    def get_context_data(self, **kwargs):
        estado = get_object_or_404(EstadoDocumento, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["estado"] = estado
        return context

    def post(self, request, *args, **kwargs):
        estado = get_object_or_404(EstadoDocumento, pk=kwargs["pk"])
        estado.nombre = request.POST.get("nombre")
        estado.color = request.POST.get("color")
        estado.save()
        return redirect("estados-lista")


class EstadoEliminarView(TemplateView):
    template_name = "estados/eliminar.html"

    def get_context_data(self, **kwargs):
        estado = get_object_or_404(EstadoDocumento, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["estado"] = estado
        return context

    def post(self, request, *args, **kwargs):
        estado = get_object_or_404(EstadoDocumento, pk=kwargs["pk"])
        estado.delete()
        return redirect("estados-lista")
