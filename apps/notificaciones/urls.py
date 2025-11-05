from django.urls import path
from .views import NotificacionListView, NotificacionCrearView

urlpatterns = [
    path("lista/", NotificacionListView.as_view(), name="notificaciones-lista"),
    path("nueva/", NotificacionCrearView.as_view(), name="notificaciones-nueva"),
]
