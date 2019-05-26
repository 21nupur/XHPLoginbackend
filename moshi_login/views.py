from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model, models
from rest_framework import generics
from . import serializer


class TokenAccessView(TokenObtainPairView):
    # renderer_classes = (CustomJSONRenderer,)
    token_obtain_pair = TokenObtainPairView.as_view()


class RefreshTokenView(TokenRefreshView):
    # renderer_classes = (CustomJSONRenderer,)
    token_refresh = TokenRefreshView.as_view()


class VerifyTokenView(TokenVerifyView):
    # renderer_classes = (CustomJSONRenderer,)
    token_verify = TokenVerifyView.as_view()

class SecuredView(APIView):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        return Response({'HI'}, status=200)