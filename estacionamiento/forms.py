from django.forms import ModelForm
from .models import registros

class registrosForm(ModelForm):
    class Meta:
        model = registros
        fields = ['espacio','marca', 'modelo','placa','estado','fecha_salida']
