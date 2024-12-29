from rest_framework import serializers
from .models import Task, User
from django.contrib.auth import authenticate

# Serializador para el modelo de Usuario personalizado
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # La contraseña no se expone en las respuestas

    def create(self, validated_data):
        """Crea un usuario y configura su contraseña correctamente"""
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hashea la contraseña
        user.save()
        return user

# Serializador para el inicio de sesión del Usuario
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Autenticar al usuario con las credenciales
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user

# Serializador para el modelo de Tareas
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Asociar al usuario autenticado

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'priority', 'due_date', 'user']
        read_only_fields = ['user']  # El usuario se gestiona automáticamente
