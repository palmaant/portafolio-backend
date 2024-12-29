from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, Task
from .serializers import UserSerializer, UserLoginSerializer, TaskSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Vista para el manejo de usuarios
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def login(self, request):
        """Vista personalizada para el inicio de sesión"""
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token = RefreshToken.for_user(user)
            return Response({
                "access": str(token.access_token),  # Token de acceso
                "refresh": str(token)               # Token de refresh
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para el manejo de tareas
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Asegura que el usuario esté autenticado

    def get_queryset(self):
        """Filtra las tareas por el usuario autenticado.
           Los superusuarios pueden ver todas las tareas"""
        user = self.request.user
        if user.is_superuser:
            return Task.objects.all()  # Si el usuario es superusuario, todas las tareas
        return Task.objects.filter(user=user)  # Si no, solo las tareas del usuario autenticado

    def perform_create(self, serializer):
        """Asocia la tarea al usuario autenticado"""
        serializer.save(user=self.request.user)
