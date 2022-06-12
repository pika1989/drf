from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import get_user_model


hardcoded_auth_token = 'Super_secret_token'


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if request.headers.get('Authorization', '') == hardcoded_auth_token:
            return get_user_model(), None

        raise exceptions.AuthenticationFailed('Invalid username/password.')
