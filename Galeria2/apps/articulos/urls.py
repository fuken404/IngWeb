from django.urls import path
from . import views

urlpatterns = [
  path("vista", views.articulos, name="articulos"),
  path("eliminar/<int:articulo_id>", views.eliminar_articulo, name="eliminar_articulo"),
  path("obtener/<int:articulo_id>", views.obtener_articulo, name="obtener_articulo"),
  path("subir/", views.subir_articulo, name="subir_articulo"),
]