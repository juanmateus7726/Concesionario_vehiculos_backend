import logging
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)


class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'detail': 'El correo es requerido.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'Si el correo existe, recibirás un enlace.'}, status=status.HTTP_200_OK)

        uid   = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        link  = f"{settings.FRONTEND_URL}/reset-password?uid={uid}&token={token}"

        send_mail(
            subject='Recuperar contraseña — Monitoring Innovation',
            message=f'Haz clic en el siguiente enlace para restablecer tu contraseña:\n\n{link}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        logger.info(f"Correo de recuperación enviado a: {email}")
        return Response({'detail': 'Si el correo existe, recibirás un enlace.'}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        uid      = request.data.get('uid')
        token    = request.data.get('token')
        password = request.data.get('password')

        if not all([uid, token, password]):
            return Response({'detail': 'Datos incompletos.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            pk   = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=pk)
        except (User.DoesNotExist, ValueError):
            return Response({'detail': 'Enlace inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({'detail': 'El enlace ha expirado o es inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(password)
        user.save()
        logger.info(f"Contraseña restablecida para: {user.username}")
        return Response({'detail': 'Contraseña actualizada correctamente.'}, status=status.HTTP_200_OK)