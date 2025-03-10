from django.db import models

# Create your models here.
class Articulo(models.Model):
  titular = models.CharField(max_length=90)
  fecha = models.DateField(auto_now_add=True)
  descripcion = models.CharField(max_length=2000)
  autor = models.CharField(max_length=90)
  imagen = models.ImageField(upload_to='imagenesNews/')
  publicado = models.BooleanField(default = True)
  
  def __str__(self):
    return self.nombre