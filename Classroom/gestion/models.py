from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Agregar related_name personalizado para evitar conflictos con el modelo auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Cambia el nombre del reverse accessor
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions_set',  # Cambia el nombre del reverse accessor
        blank=True,
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'password']

    def __str__(self):
        return self.nombre

    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField(null=True, blank=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')
    colaboradores = models.ManyToManyField(Usuario, related_name='proyectos_asignados')

    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    ESTADO_OPCIONES = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='Pendiente')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    hora_vencimiento = models.TimeField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')
    usuarios_asignados = models.ManyToManyField(Usuario, through='AsignacionTarea')
    etiquetas = models.ManyToManyField('Etiqueta', related_name='tareas')

    def __str__(self):
        return self.titulo

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

class AsignacionTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tarea} - {self.usuario}'

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f'Comentario de {self.autor} en {self.tarea}'


