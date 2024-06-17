from rest_framework import serializers

from bbms.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ['date']
        depth = 1
