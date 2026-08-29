from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("activate/<str:token>/", views.ActivateAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("profile/", views.ProfileAPIView.as_view()),
    path("password-reset/", views.PasswordResetRequestAPIView.as_view()),
    path("password-reset/confirm/", views.PasswordResetConfirmAPIView.as_view()),
]
