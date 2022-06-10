from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, viewsets

from .models import Group, User
from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UsersInGroupViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_pk']
        if 'user_pk' in self.kwargs:
            user_pk = self.kwargs['user_pk']
            return User.objects.filter(id=user_pk)

        return User.objects.filter(group_id=group_id)

    def update(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        group_id = self.kwargs['group_pk']
        user = User.objects.get(id=user_id)
        group = Group.objects.get(id=group_id)
        group.user_set.add(user)

        return Response({'success': 200}, status=status.HTTP_200_OK)
