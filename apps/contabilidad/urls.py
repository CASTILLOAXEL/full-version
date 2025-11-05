# apps/contabilidad/urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    MovimientosListView,
    MovimientoNuevoView,
    ReporteContableView,
    exportar_excel,
    exportar_pdf
)

urlpatterns = [
    path("lista/", login_required(MovimientosListView.as_view()), name="contabilidad-lista"),
    path("nuevo/", login_required(MovimientoNuevoView.as_view()), name="contabilidad-nuevo"),
    path("reportes/", login_required(ReporteContableView.as_view()), name="contabilidad-reportes"),
    path("exportar-excel/", login_required(exportar_excel), name="contabilidad-exportar-excel"),
    path("exportar-pdf/", login_required(exportar_pdf), name="contabilidad-exportar-pdf"),
]
