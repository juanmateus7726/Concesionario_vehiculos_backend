import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .serializers import RegisterSerializer, UserSerializer

logger = logging.getLogger(__name__)


class RegisterView(APIView):
    permission_classes = [AllowAny]  # No requiere estar logueado

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f"Usuario registrado: {user.username} rol={user.role}")
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            logger.warning(f"Login fallido para: {username}")
            return Response(
                {'detail': 'Credenciales inválidas'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Generamos los tokens JWT
        refresh = RefreshToken.for_user(user)
        logger.info(f"Login exitoso: {user.username} rol={user.role}")

        return Response({
            'access': str(refresh.access_token),   # token de corta vida (60 min)
            'refresh': str(refresh),                # token para renovar
            'user': UserSerializer(user).data,
        })