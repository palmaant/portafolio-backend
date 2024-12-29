from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer, UserLoginSerializer

# ViewSet para las tareas
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

# Vista para el login de usuario
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = RefreshToken.for_user(user)
            return Response({
                'access': str(token.access_token),  # Token de acceso
                'refresh': str(token),  # Token de refresco
            }, status=200)  # HTTP_200_OK
        return Response(serializer.errors, status=400)  # HTTP_400_BAD_REQUEST
