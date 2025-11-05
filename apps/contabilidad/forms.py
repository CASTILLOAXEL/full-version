# apps/contabilidad/forms.py
from django import forms
from .models import MovimientoContable

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = MovimientoContable
        fields = ['cliente', 'tipo', 'monto', 'descripcion']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

        }
