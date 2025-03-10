from django.db import models

# Create your models here.
class Foto(models.Model):
  nombre = models.CharField(max_length=90)
  descripcion = models.CharField(max_length=2000)
  imagen = models.ImageField(upload_to='imagenes/')
  #imageurl = models.CharField(max_length=120)
  publicado = models.BooleanField(default = True)
  
  def __str__(self):
    return self.nombre