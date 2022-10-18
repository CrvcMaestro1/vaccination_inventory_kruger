from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from transactions.serializers.auth_serializer import AuthTokenResponseSerializer
from transactions.services.default_auth_service import DefaultAuthService


class AuthView(ObtainAuthToken):
    service = DefaultAuthService()

    @swagger_auto_schema(
        tags=["auth"],
        request_body=AuthTokenSerializer,
        responses={
            status.HTTP_200_OK: AuthTokenResponseSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad request"
        }
    )
    def post(self, request, *args, **kwargs):
        return self.service.auth(request)


class LogoutView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    service = DefaultAuthService()

    @swagger_auto_schema(
        tags=["auth"],
        responses={
            status.HTTP_200_OK: "200 OK",
            status.HTTP_400_BAD_REQUEST: "Bad request"
        }
    )
    def post(self, request, *args, **kwargs):
        return self.service.logout(request)
