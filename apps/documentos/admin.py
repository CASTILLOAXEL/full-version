from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CategoriaDocumento, EstadoDocumento, Documento

admin.site.register(CategoriaDocumento)
admin.site.register(EstadoDocumento)
admin.site.register(Documento)
