from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Group, Members, User
from .serializers import GroupSerializer, MembersSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data

        user.login = data.get('login', user.login)
        user.sex = data.get('sex', user.sex)
        user.birth_date = data.get('birth_date', user.birth_date)

        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MembersViewSet(viewsets.ModelViewSet):
    serializer_class = MembersSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_pk']

        members = Members.objects.filter(group_id=group_id)
        users_id = []
        for member in members:
            users_id.append(member.user_id)

        if 'user_pk' in self.kwargs:
            user_pk = self.kwargs['user_pk']
            if user_pk in users_id:
                return User.objects.filter(id=user_pk)

        return User.objects.filter(id__in=users_id)

    def create(self, request, *args, **kwargs):
        user_id = request.data['user']
        group_id = self.kwargs['group_pk']
        Members.objects.create(user_id=user_id, group_id=group_id)

        return Response({'success': 200}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user_id = self.kwargs['user_pk']
        group_id = self.kwargs['group_pk']
        member = Members.objects.filter(group_id=group_id).filter(user_id=user_id)
        member.delete()

        return Response({'success': 200}, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)

        if 'user_pk' in self.kwargs:
            user_id = self.kwargs['user_pk']
            group_id = self.kwargs['group_pk']
            member = Members.objects.filter(group_id=group_id).filter(user_id=user_id)
            if not member:
                return Response({'Page not found': 404}, status=status.HTTP_404_NOT_FOUND)

            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        return Response(serializer.data)
