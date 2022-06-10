from rest_framework import serializers

from .models import Group, Members, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'public',)


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField('get_user_groups')

    class Meta:
        model = User
        fields = ('id', 'login', 'sex', 'birth_date', 'groups')

    def get_user_groups(self, obj):
        members_data = Members.objects.filter(user_id=obj.id)
        groups = []
        for member_data in members_data:
            groups.append(member_data.group_id)

        return groups


class MembersSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_users_list')

    class Meta:
        model = Members
        fields = ('user',)

    def get_users_list(self, obj):
        users = User.objects.filter(id=obj.id)
        return UserSerializer(users, many=True).data
