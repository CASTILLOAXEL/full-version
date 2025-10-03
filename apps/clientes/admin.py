from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cliente, TipoCliente

admin.site.register(Cliente)
admin.site.register(TipoCliente)
