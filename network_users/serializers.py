from rest_framework import serializers

from .models import Group, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'public',)


class UserSerializer(serializers.ModelSerializer):
#    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    class Meta:
        model = User
        fields = ('id', 'login', 'sex', 'birth_date', 'group')
 #       read_only_fields = ['login']
