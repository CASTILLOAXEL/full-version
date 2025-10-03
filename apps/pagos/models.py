from django.db import models

# Create your models here.
from django.db import models
from apps.clientes.models import Cliente  # Importamos Cliente

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    estado = models.CharField(max_length=50, default="Pendiente")

    def __str__(self):
        return f"{self.cliente.nombre} - {self.servicio.nombre} ({self.monto})"
