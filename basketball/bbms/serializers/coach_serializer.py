from rest_framework import serializers

from bbms.models import Coach


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'
        depth = 1
