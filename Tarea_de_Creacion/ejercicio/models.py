from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    fecha_registro=models.DateTimeField(default=timezone.now)

class Proyecto(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(max_length=2500) 
    duracion=models.FloatField()
    fecha_inicio=models.DateField(default=timezone.now)
    fecha_fin=models.DateField(default=timezone.now)
    
    colaboradores=models.ManyToManyField(Usuario,related_name='colaboradores_proyecto')
    
    creador=models.ForeignKey(Usuario,related_name='creador_proyecto',on_delete=models.CASCADE)
    
class Tarea(models.Model):
    titulo=models.CharField(max_length=100) 
    descripcion=models.TextField()
    prioridad=models.IntegerField()
    
    ESTADOS=[('PE','Pendiente'),('PR','Progreso'),('Co','Completada')]
    estado=models.CharField(max_length=2,choices=ESTADOS)
    
    completada=models.BooleanField()
    fecha_creacion=models.DateField(default=timezone.now)
    hora_vencimiento=models.TimeField(default=timezone.now)
    
    creador=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="creador_tarea")
    

    usuarios_asignados=models.ManyToManyField(Usuario, through='asignacionTarea',
                                            related_name='colaboradores_tarea')

    proyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE,related_name="proyecto_tareas")

class AsignacionTarea(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE)
    observaciones=models.TextField(max_length=2500)
    fecha_asignacion=models.DateTimeField(default=timezone.now)

class Etiqueta(models.Model):
    nombre=models.CharField(max_length=30,unique=True)
    tarea=models.ManyToManyField(Tarea,related_name="etiquetas_tareas")

class Comentario(models.Model):
    contenido=models.TextField(max_length=2500)
    fecha_comentario=models.DateTimeField(default=timezone.now)
    
    autor=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="comentarios_creador")
    
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE,related_name="comentarios_tarea")