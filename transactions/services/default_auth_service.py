from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from transactions.services.interfaces.auth_service import AuthService


class DefaultAuthService(AuthService):
    serializer_class = AuthTokenSerializer

    def auth(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'email': user.email}, status=status.HTTP_200_OK)

    def logout(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
