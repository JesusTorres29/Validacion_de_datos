from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'api', ProductoViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('agregar/', agregar_prodcuto, name='agregar_producto'),
]
