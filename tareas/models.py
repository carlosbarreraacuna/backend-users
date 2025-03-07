from django.db import models
from personas.models import Persona

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tareas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo