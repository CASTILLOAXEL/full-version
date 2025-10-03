# from django.urls import path
# from .views import ClientesListView, ClienteNuevoView
# from django.contrib.auth.decorators import login_required
#
# urlpatterns = [
#     path("lista/", login_required(ClientesListView.as_view()), name="clientes-lista"),
#     path("nuevo/", login_required(ClienteNuevoView.as_view()), name="clientes-nuevo"),
# ]
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    ClientesListView, ClienteNuevoView, ClienteEditarView,
    ClienteEliminarView, ClienteDetalleView
)

urlpatterns = [
    path("lista/", login_required(ClientesListView.as_view()), name="clientes-lista"),
    path("nuevo/", login_required(ClienteNuevoView.as_view()), name="clientes-nuevo"),
    path("editar/<int:pk>/", login_required(ClienteEditarView.as_view()), name="clientes-editar"),
    path("eliminar/<int:pk>/", login_required(ClienteEliminarView.as_view()), name="clientes-eliminar"),
    path("detalle/<int:pk>/", login_required(ClienteDetalleView.as_view()), name="clientes-detalle"),
]
