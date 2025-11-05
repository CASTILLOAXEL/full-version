from django.urls import path,include
from django.contrib.auth.decorators import login_required
from .views import (
    DocumentosListView, DocumentoNuevoView, DocumentoEditarView,
    DocumentoEliminarView, DocumentoDetalleView
)

urlpatterns = [
    path("lista/", login_required(DocumentosListView.as_view()), name="documentos-lista"),
    path("subir/", login_required(DocumentoNuevoView.as_view()), name="documentos-subir"),
    path("editar/<int:pk>/", login_required(DocumentoEditarView.as_view()), name="documentos-editar"),
    path("eliminar/<int:pk>/", login_required(DocumentoEliminarView.as_view()), name="documentos-eliminar"),
    path("detalle/<int:pk>/", login_required(DocumentoDetalleView.as_view()), name="documentos-detalle"),

    path("categorias/", include("apps.documentos.urls_categorias")),
     path("estados/", include("apps.documentos.urls_estados")),

]
