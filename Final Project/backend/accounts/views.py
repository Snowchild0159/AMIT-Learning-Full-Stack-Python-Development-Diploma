from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
)
from .tokens import make_token, check_token


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        token = make_token(user.id, "activate")
        link = f"{settings.FRONTEND_URL}/activate/{token}"
        send_mail(
            "Activate your Mahally account",
            f"Welcome to Mahally! Click the link to activate your account (valid for 24 hours):\n{link}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )


class ActivateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        user_id = check_token(token, "activate")
        if user_id is None:
            return Response({"detail": "Invalid or expired activation link."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        user.is_active = True
        user.save()
        return Response({"detail": "Account activated. You can log in now."})


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class PasswordResetRequestAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # same answer either way, so nobody can guess which emails exist
            return Response({"detail": "If this email exists, a reset link was sent."})
        token = make_token(user.id, "reset")
        link = f"{settings.FRONTEND_URL}/reset-password/{token}"
        send_mail(
            "Reset your Mahally password",
            f"Click the link to choose a new password (valid for 24 hours):\n{link}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )
        return Response({"detail": "If this email exists, a reset link was sent."})


class PasswordResetConfirmAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = check_token(serializer.validated_data["token"], "reset")
        if user_id is None:
            return Response({"detail": "Invalid or expired reset link."}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(id=user_id)
        user.set_password(serializer.validated_data["password"])
        user.save()
        return Response({"detail": "Password changed. You can log in now."})
