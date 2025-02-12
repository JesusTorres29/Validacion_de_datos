from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import PermissionDenied

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]

    # Seguridad con JWT
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user)  # Aquí puedes imprimir el usuario autenticado
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated()]
        return []

    def perform_destroy(self, instance):
        if instance == self.request.user:
            raise PermissionDenied("No puedes eliminar tu propio usuario.")  
        super().perform_destroy(instance)

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CustomUserFormAPI(APIView):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        fields = {
            field: {
            'label': form[field].label,
            'input':form[field].field.widget.attrs,
            'type': form[field].field.widget.input_type,
            }
                for field in form.fields
        }
        return Response(fields)
    
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.data)
        if form.is_valid():
            user_data = form.cleaned_data
            User = get_user_model()
            user = User.objects.create_user(
            email=user_data['email'],
            password=user_data['password1'],
            name=user_data['name'],
            surname=user_data['surname'],
            control_number=user_data['control_number'],
            age=user_data['age'],
            tel=user_data['tel'],
            )
            return Response({'message': 'Usuario creado con éxito'},status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)