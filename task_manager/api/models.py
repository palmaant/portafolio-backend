from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuario extendido
class User(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Evita conflictos con el modelo por defecto
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Evita conflictos con el modelo por defecto
        blank=True
    )

# Modelo de Tarea
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, default='low')
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # Agrega related_name

    def __str__(self):
        return self.title
