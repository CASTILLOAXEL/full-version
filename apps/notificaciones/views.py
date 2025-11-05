from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from web_project import TemplateLayout
from .models import Notificacion
from .forms import NotificacionForm

class NotificacionListView(LoginRequiredMixin, TemplateView):
    template_name = "notificaciones/lista.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        usuario = self.request.user
        context["notificaciones"] = Notificacion.objects.filter(usuario=usuario)
        return context


class NotificacionCrearView(LoginRequiredMixin, TemplateView):
    template_name = "notificaciones/form.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = NotificacionForm()
        return context

    def post(self, request, *args, **kwargs):
        form = NotificacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Notificación creada correctamente.")
            return redirect("notificaciones-lista")

        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = form
        return self.render_to_response(context)
