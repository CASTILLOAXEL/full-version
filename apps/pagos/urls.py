from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    PagosListView, PagoNuevoView, PagoEditarView,
    PagoEliminarView, PagoDetalleView
)

urlpatterns = [
    path("lista/", login_required(PagosListView.as_view()), name="pagos-lista"),
    path("registrar/", login_required(PagoNuevoView.as_view()), name="pagos-registrar"),
    path("editar/<int:pk>/", login_required(PagoEditarView.as_view()), name="pagos-editar"),
    path("eliminar/<int:pk>/", login_required(PagoEliminarView.as_view()), name="pagos-eliminar"),
    path("detalle/<int:pk>/", login_required(PagoDetalleView.as_view()), name="pagos-detalle"),
]
