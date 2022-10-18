from rest_framework import views
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from transactions.services.default_auth_service import DefaultAuthService


class AuthView(ObtainAuthToken):
    service = DefaultAuthService()

    def post(self, request, *args, **kwargs):
        return self.service.auth(request)


class LogoutView(views.APIView):
    authentication_classes = [TokenAuthentication]
    service = DefaultAuthService()

    def post(self, request, *args, **kwargs):
        return self.service.logout(request)
