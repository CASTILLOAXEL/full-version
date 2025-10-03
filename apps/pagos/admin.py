from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Servicio, Pago

admin.site.register(Servicio)
admin.site.register(Pago)
