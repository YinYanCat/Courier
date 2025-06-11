from django import forms
from app.models import DeliveryOrder, Warehouse

class OrderForm(forms.Form):
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        label="Oficina de Correos"
    )	
    destination = forms.CharField(max_length=200, required=True, label="Dirección de destino")
    dim_x = forms.FloatField(required=True, label="Ancho (cm)")
    dim_y = forms.FloatField(required=True, label="Alto (cm)")
    dim_z = forms.FloatField(required=True, label="Largo (cm)")
    weight = forms.FloatField(required=True, label="Peso (kg)")