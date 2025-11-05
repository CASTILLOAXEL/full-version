from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps.pagos.models import Pago
from apps.documentos.models import Documento
from .models import Notificacion


# 🧾 Cuando se crea un Pago → Notificar al administrador
@receiver(post_save, sender=Pago)
def notificar_pago_creado(sender, instance, created, **kwargs):
    if created:
        # Buscar usuario administrador
        admin = User.objects.filter(is_superuser=True).first()
        if admin:
            Notificacion.objects.create(
                usuario=admin,
                titulo="💵 Nuevo Pago Registrado",
                mensaje=f"El cliente {instance.cliente.nombre} ha realizado un pago de Q{instance.monto}.",
                tipo="administrador"
            )


# 📄 Cuando se sube un Documento → Notificar al administrador
@receiver(post_save, sender=Documento)
def notificar_documento_subido(sender, instance, created, **kwargs):
    if created:
        admin = User.objects.filter(is_superuser=True).first()
        if admin:
            Notificacion.objects.create(
                usuario=admin,
                titulo="📂 Nuevo Documento Subido",
                mensaje=f"El cliente {instance.cliente.nombre} ha subido un documento: {instance.categoria.nombre}.",
                tipo="administrador"
            )
