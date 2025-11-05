from django.urls import path
from django.contrib.auth.decorators import login_required
from .views_categorias import (
    CategoriaListView,
    CategoriaNuevaView,
    CategoriaEditarView,
    CategoriaEliminarView,
)

urlpatterns = [
    path("", login_required(CategoriaListView.as_view()), name="categorias-lista"),
    path("nueva/", login_required(CategoriaNuevaView.as_view()), name="categorias-nueva"),
    path("editar/<int:pk>/", login_required(CategoriaEditarView.as_view()), name="categorias-editar"),
    path("eliminar/<int:pk>/", login_required(CategoriaEliminarView.as_view()), name="categorias-eliminar"),
]

