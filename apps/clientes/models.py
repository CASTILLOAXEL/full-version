# from django.db import models
#
# # Create your models here.
# from django.db import models
#
# class TipoCliente(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.nombre
#
#
# class Cliente(models.Model):
#     nombre = models.CharField(max_length=150)
#     nit = models.CharField(max_length=20, unique=True)
#     telefono = models.CharField(max_length=20, null=True, blank=True)
#     correo = models.EmailField(max_length=100, null=True, blank=True)
#     direccion = models.CharField(max_length=255, null=True, blank=True)
#     tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE)
#     creado_en = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.nombre} - {self.nit}"
#
#
from django.db import models

class TipoCliente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    TIPO_CONTRIBUYENTE = [
        ('PEQUEÑO', 'Pequeño Contribuyente'),
        ('MEDIANO', 'Mediano Contribuyente'),
    ]

    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE, null=True, blank=True)
    tipo_contribuyente = models.CharField(max_length=20, choices=TIPO_CONTRIBUYENTE, default='PEQUEÑO')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_contribuyente_display()})"
