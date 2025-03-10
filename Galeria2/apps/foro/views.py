from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Mensaje
import random
import hashlib

USERNAMES = ["CapybaraAnonymus", "SecretUser", "LonelyWolf", "CyberNinja", "FreeThinker"]

def obtener_username(ip):
    hash_object = hashlib.md5(ip.encode())
    index = int(hash_object.hexdigest(), 16) % len(USERNAMES)
    return USERNAMES[index]

def foro_view(request):
    mensajes = Mensaje.objects.all().order_by("-fecha")
    return render(request, "foro/foro.html", {"mensajes": mensajes})

def publicar_mensaje(request):
    if request.method == "POST":
        contenido = request.POST.get("contenido")
        ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
        username = obtener_username(ip)
        
        mensaje = Mensaje.objects.create(username=username, contenido=contenido)
        return redirect("foro")

def dar_like(request, mensaje_id):
    mensaje = Mensaje.objects.get(id=mensaje_id)
    mensaje.likes += 1
    mensaje.save()
    return JsonResponse({"likes": mensaje.likes})
