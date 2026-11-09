# models: trae las herramientas de Django para describir tablas como clases
from django.db import models
# User: el modelo de usuario que Django ya trae incluido (login, contraseñas, sesiones)
from django.contrib.auth.models import User

# class Servicio: se convierte en la tabla "core_servicio" dentro de MySQL
class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']
def __str__(self):
    return self.nombre

class Servicio(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=60)
    categoria_ref = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, related_name='servicios')
    creado_en = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
