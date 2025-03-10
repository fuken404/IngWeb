from django.urls import path
from . import views

urlpatterns = [
  path("visor", views.fotos, name="fotos"),
  path("eliminar/<int:foto_id>", views.eliminar_fotos, name="eliminar_foto"),
  path("subir/", views.subir_foto, name="subir_foto")
]