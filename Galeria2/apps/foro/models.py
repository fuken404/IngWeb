from django.db import models
import random
import hashlib

USERNAMES = ["CapybaraAnonymus", "SecretUser", "LonelyWolf", "CyberNinja", "FreeThinker"]

class Mensaje(models.Model):
    username = models.CharField(max_length=50, editable=False)
    contenido = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = random.choice(USERNAMES)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.username}: {self.contenido[:30]}"