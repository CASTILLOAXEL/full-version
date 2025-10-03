from django import forms
from .models import Pago

from django import forms
from .models import Pago, Servicio, Cliente

class PagoForm(forms.ModelForm):
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione un servicio"
    )

    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione un cliente"
    )

    class Meta:
        model = Pago
        fields = ['cliente', 'servicio', 'monto', 'fecha_pago', 'estado']
        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_pago': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    # 👇 Aquí personalizamos la etiqueta de los servicios
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicio'].label_from_instance = (
            lambda obj: f"{obj.nombre} — Q{obj.precio}"
        )
