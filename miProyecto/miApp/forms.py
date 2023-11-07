from django import forms
from django.core.exceptions import ValidationError
from .models import Producto

def validate_positive_price(value):
    if value <= 0:
        raise ValidationError('El precio debe ser mayor que cero.')

class ProductoForm(forms.ModelForm):
    precio = forms.DecimalField(validators=[validate_positive_price])
    
    class Meta:
        model = Producto
        fields = '__all__'

