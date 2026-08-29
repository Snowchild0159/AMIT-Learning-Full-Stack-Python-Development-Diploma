from django.urls import path
from . import views


urlpatterns = [
    path('register/' , views.UsersAPIView.as_view())
]
