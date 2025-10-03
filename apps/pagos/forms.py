from django import forms
from .models import Pago

from django import forms
from .models import Pago, Cliente, Servicio

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['cliente', 'servicio', 'monto', 'fecha_pago', 'estado']

        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_pago': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
