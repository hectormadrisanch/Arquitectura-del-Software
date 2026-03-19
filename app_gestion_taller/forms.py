from django import forms
from .models import Cliente, Coche, Servicio, CocheServicio

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = '__all__'

# Para crear solo el tipo de servicio (ej: Lavado)
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion'] 

# Para asignar un servicio a un coche concreto
class ContratarServicioForm(forms.ModelForm):
    class Meta:
        model = CocheServicio
        fields = ['coche', 'servicio']
        