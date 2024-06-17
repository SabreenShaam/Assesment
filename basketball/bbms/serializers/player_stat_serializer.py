from rest_framework import serializers

from bbms.models import Player_Stat


class PlayerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player_Stat
        fields = '__all__'
        depth = 1
