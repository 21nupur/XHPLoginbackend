from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from . import serializer
from .models import CustomUser
from datetime import datetime


class RegisterUser(generics.CreateAPIView):
    model = CustomUser
    permission_classes = [AllowAny]
    serializer_class = serializer.UserSerializer


class UserDetailsView(generics.ListAPIView):
    serializer_class = serializer.UserDetailSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def get_queryset(self):
        username = self.request.user.username
        user = CustomUser.objects.filter(username=username)
        user.update(last_login=datetime.now())
        return user