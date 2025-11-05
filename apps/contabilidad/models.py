from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.clientes.models import Cliente
from apps.pagos.models import Pago


class MovimientoContable(models.Model):
    TIPO_CHOICES = [
        ("Ingreso", "Ingreso"),
        ("Egreso", "Egreso"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, null=True, blank=True, related_name="movimientos")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - Q{self.monto} ({self.fecha})"


@receiver(post_save, sender=Pago)
def crear_movimiento_contable(sender, instance, created, **kwargs):
    if created:
        MovimientoContable.objects.create(
            cliente=instance.cliente,
            pago=instance,
            tipo="Ingreso",
            monto=instance.monto,
            descripcion=f"Pago de servicio: {instance.servicio.nombre}",
        )
