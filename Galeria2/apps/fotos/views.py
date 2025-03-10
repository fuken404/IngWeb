from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Foto

# Create your views here.
def fotos(request):
  fotos_subidas = Foto.objects.all()
  return render(request, 'fotos/fotos.html', {"fotos": fotos_subidas})

def eliminar_fotos(request, foto_id):
  foto = get_object_or_404(Foto, id=foto_id)
  foto.delete()
  return redirect('fotos')

def subir_foto(request):
    if request.method == "POST" and request.FILES.get("imagen"):
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES["imagen"]

        nueva_foto = Foto(nombre=nombre, descripcion=descripcion, imagen=imagen)
        nueva_foto.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "Método no permitido"})