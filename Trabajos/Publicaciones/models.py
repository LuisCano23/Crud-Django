from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class publicaciones(models.Model):
    titulo=models.CharField(max_length=120)
    descripcion=models.TextField(blank=True)
    fecha=models.DateTimeField(auto_now_add=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' POR: ' + self.usuario.username