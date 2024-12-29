from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserLoginView

# Router para las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API para las tareas
    path('api/login/', UserLoginView.as_view(), name='user-login'),  # Login de usuario
]
