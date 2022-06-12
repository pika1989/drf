from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import get_user_model


hardcoded_auth_token = 'Super_secret_token'


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            if request.headers.get('Authorization', 'Bearer ').split('Bearer ')[1] == hardcoded_auth_token:
                return get_user_model(), None
        except IndexError:
            raise exceptions.AuthenticationFailed('Invalid token type. Use Bearer token.')

        raise exceptions.AuthenticationFailed('Invalid auth token provided.')
