from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuario extendido
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Campo de email único

    # Relación ManyToMany con los grupos, evita conflictos con el modelo por defecto
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    
    # Relación ManyToMany con los permisos, evita conflictos con el modelo por defecto
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    def __str__(self):
        return self.username  # Retorna el nombre de usuario como representación del objeto

# Modelo de Tarea
class Task(models.Model):
    # Título de la tarea
    title = models.CharField(max_length=100)

    # Descripción de la tarea (opcional)
    description = models.TextField(blank=True, null=True)

    # Estado de la tarea (completada o no)
    completed = models.BooleanField(default=False)

    # Prioridad de la tarea (baja, media, alta)
    priority = models.CharField(max_length=10, choices=[
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta')
    ], default='low')

    # Fecha límite para completar la tarea (opcional)
    due_date = models.DateTimeField(null=True, blank=True)

    # Relación con el modelo de usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title  # Representación del objeto como título de la tarea
