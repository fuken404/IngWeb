from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Articulo

# Create your views here.
def articulos(request):
  articulo_subidas = Articulo.objects.all()
  return render(request, 'articulo/articulo.html', {"articulos": articulo_subidas})

def obtener_articulo(request, articulo_id):
  articulo = get_object_or_404(Articulo, id=articulo_id)
  data = {
    "id": articulo.id,
    "titular": articulo.titular,
    "descripcion": articulo.descripcion,
    "autor": articulo.autor,
    "fecha": articulo.fecha.strftime("%Y-%m-%d"),
    "imagen": articulo.imagen.url
  }
  return JsonResponse(data)
  

def eliminar_articulo(request, articulo_id):
  articulo = get_object_or_404(Articulo, id=articulo_id)
  articulo.delete()
  return redirect('articulos')

def subir_articulo(request):
    if request.method == "POST" and request.FILES.get("imagen"):
        titular = request.POST.get("titular")
        #fecha = request.POST.get("fecha")
        descripcion = request.POST.get("descripcion")
        autor = request.POST.get("autor")
        imagen = request.FILES["imagen"]

        nuevo_articulo = Articulo(titular=titular, descripcion=descripcion, autor=autor,imagen=imagen)
        nuevo_articulo.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "Método no permitido"})