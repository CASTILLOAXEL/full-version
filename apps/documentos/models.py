# from django.db import models
#
# # Create your models here.
# from django.db import models
# from apps.clientes.models import Cliente
# from django.contrib.auth.models import User
#
# class CategoriaDocumento(models.Model):
#     nombre = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.nombre
#
#
# class EstadoDocumento(models.Model):
#     nombre = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.nombre
#
#
# class Documento(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     categoria = models.ForeignKey(CategoriaDocumento, on_delete=models.CASCADE)
#     estado = models.ForeignKey(EstadoDocumento, on_delete=models.CASCADE)
#     archivo = models.FileField(upload_to="documentos/")  # Se guarda en MEDIA_ROOT/documentos/
#     version = models.IntegerField(default=1)
#     subido_por = models.ForeignKey(User, on_delete=models.CASCADE)
#     fecha = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.archivo} - {self.cliente.nombre}"
from django.db import models
from apps.clientes.models import Cliente
from django.contrib.auth.models import User

class CategoriaDocumento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class EstadoDocumento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Documento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaDocumento, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.ForeignKey(EstadoDocumento, on_delete=models.SET_NULL, null=True, blank=True)
    archivo = models.FileField(upload_to="documentos/")  # MEDIA_ROOT/documentos/
    version = models.IntegerField(default=1)
    subido_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.archivo.name} - {self.cliente.nombre}"
