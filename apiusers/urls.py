from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from personas.views import PersonaViewSet
from tareas.views import TareaViewSet

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]