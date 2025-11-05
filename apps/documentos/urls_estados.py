from django.urls import path
from django.contrib.auth.decorators import login_required
from .views_estados import (
    EstadoListView,
    EstadoNuevoView,
    EstadoEditarView,
    EstadoEliminarView,
)

urlpatterns = [
    path("", login_required(EstadoListView.as_view()), name="estados-lista"),
    path("nueva/", login_required(EstadoNuevoView.as_view()), name="estados-nueva"),
    path("editar/<int:pk>/", login_required(EstadoEditarView.as_view()), name="estados-editar"),
    path("eliminar/<int:pk>/", login_required(EstadoEliminarView.as_view()), name="estados-eliminar"),
]
