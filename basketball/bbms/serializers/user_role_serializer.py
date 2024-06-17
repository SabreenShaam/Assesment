from rest_framework import serializers

from bbms.models import User_Role


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Role
        exclude = ['user']
        depth = 1
