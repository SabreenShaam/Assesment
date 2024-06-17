from rest_framework import serializers

from bbms.models import User_Stat


class UserStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Stat
        exclude = ['user']
        depth = 1
