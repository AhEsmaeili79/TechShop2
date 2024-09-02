from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Token

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        # Extract token after the prefix "Token"
        try:
            token = auth_header.split(' ')[1]
        except IndexError:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')

        try:
            token_obj = Token.objects.get(token=token)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if token_obj.is_expired():
            raise AuthenticationFailed('Token has expired')

        return (token_obj.user, token_obj)
