from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import CategoriaDocumento


class CategoriaListView(TemplateView):
    template_name = "categorias/lista.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["categorias"] = CategoriaDocumento.objects.all().order_by("nombre")
        return context


class CategoriaNuevaView(TemplateView):
    template_name = "categorias/nueva.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        if nombre:
            CategoriaDocumento.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect("categorias-lista")


class CategoriaEditarView(TemplateView):
    template_name = "categorias/editar.html"

    def get_context_data(self, **kwargs):
        categoria = get_object_or_404(CategoriaDocumento, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["categoria"] = categoria
        return context

    def post(self, request, *args, **kwargs):
        categoria = get_object_or_404(CategoriaDocumento, pk=kwargs["pk"])
        categoria.nombre = request.POST.get("nombre")
        categoria.descripcion = request.POST.get("descripcion")
        categoria.save()
        return redirect("categorias-lista")


class CategoriaEliminarView(TemplateView):
    template_name = "categorias/eliminar.html"

    def get_context_data(self, **kwargs):
        categoria = get_object_or_404(CategoriaDocumento, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["categoria"] = categoria
        return context

    def post(self, request, *args, **kwargs):
        categoria = get_object_or_404(CategoriaDocumento, pk=kwargs["pk"])
        categoria.delete()
        return redirect("categorias-lista")
