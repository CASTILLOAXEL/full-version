from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import Pago
from .forms import PagoForm


class PagosListView(TemplateView):
    template_name = "pagos/lista.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["pagos"] = Pago.objects.all()
        return context


class PagoNuevoView(TemplateView):
    template_name = "pagos/registrar.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = PagoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pagos-lista")

        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = form
        return self.render_to_response(context)


class PagoEditarView(TemplateView):
    template_name = "pagos/editar.html"

    def get_context_data(self, **kwargs):
        pago = get_object_or_404(Pago, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = PagoForm(instance=pago)
        context["pago"] = pago
        return context

    def post(self, request, *args, **kwargs):
        pago = get_object_or_404(Pago, pk=kwargs["pk"])
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return redirect("pagos-lista")

        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["form"] = form
        context["pago"] = pago
        return self.render_to_response(context)


class PagoEliminarView(TemplateView):
    template_name = "pagos/eliminar.html"

    def get_context_data(self, **kwargs):
        pago = get_object_or_404(Pago, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["pago"] = pago
        return context

    def post(self, request, *args, **kwargs):
        pago = get_object_or_404(Pago, pk=kwargs["pk"])
        pago.delete()
        return redirect("pagos-lista")


class PagoDetalleView(TemplateView):
    template_name = "pagos/detalle.html"

    def get_context_data(self, **kwargs):
        pago = get_object_or_404(Pago, pk=kwargs["pk"])
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["pago"] = pago
        return context
