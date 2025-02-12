from django.urls import path
from .views import*
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter
from django.urls import include

router = SimpleRouter()
router.register(r'api', CustomUserViewSet)
urlpatterns =[
    path('', include(router.urls)),
    #path para iniciar sesion
    path('token/',CustomTokenObtainPairSerializer, name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]