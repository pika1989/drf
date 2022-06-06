from rest_framework import generics
from django.shortcuts import render

from .models import User
from .serializers import UserSerializer


class UserAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPICreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
