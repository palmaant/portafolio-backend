from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Crear el router y registrar los viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)  # Registrar UserViewSet
router.register(r'tasks', TaskViewSet, basename='task')  # Registrar TaskViewSet con basename

# Configuración de las URLs
urlpatterns = [
    path('', include(router.urls)),  # Incluir todas las URLs del router
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/login/', UserViewSet.as_view({'post': 'login'}), name='login'),
]
