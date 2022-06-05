from rest_framework import generics
from django.shortcuts import render

from .models import User
from .serializers import UserSerializer


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer