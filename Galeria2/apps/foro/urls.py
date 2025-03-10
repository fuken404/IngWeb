from django.urls import path
from . import views

urlpatterns = [
    path("", views.foro_view, name="foro"),
    path("publicar/", views.publicar_mensaje, name="publicar_mensaje"),
    path("like/<int:mensaje_id>/", views.dar_like, name="dar_like"),
]
