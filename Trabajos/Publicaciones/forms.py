from django.forms import ModelForm 
from .models import publicaciones

class formPubli(ModelForm):
    class Meta:
        model = publicaciones
        fields = ['titulo', 'descripcion']