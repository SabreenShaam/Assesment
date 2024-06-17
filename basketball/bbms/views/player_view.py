import logging

from django.db.models import Avg
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from bbms.exceptions import PlayerDoesNotExistException, RoleDoesNotHaveAccessException, UserDoesNotExistException
from bbms.helper import populate_pagination
from bbms.models import Player, Player_Stat, User_Role
from bbms.serializers.player_serializer import PlayerSerializer, PlayerListSerializer
from bbms.serializers.player_stat_serializer import PlayerStatSerializer


class PlayerDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    logger = logging.getLogger(__name__)

    def get(self, request, player_id=None):
        player = Player.objects.filter(id=player_id).first()
        if player is None:
            message = "Invalid player id"
            self.logger.debug(f"Invalid player id: {player_id}")
            raise PlayerDoesNotExistException("400", "Player does not exist", message)
        player_serializer = PlayerSerializer(instance=player).data
        stat = Player_Stat.objects.filter(player_id=player_id)
        players_stat_serializer = PlayerStatSerializer(stat, many=True)
        player_object = {
            'player': player_serializer['user']['first_name'] + ' ' + player_serializer['user']['last_name'],
            'player_id': player_serializer['id'],
            'player_height': player_serializer['height'],
            'team': player.team.name,
            'games': len(players_stat_serializer.data),
            'average_score': Player_Stat.objects.filter(player_id=player_id).aggregate(Avg('score'))['score__avg'] if len(list(stat)) != 0 else 0.0
        }
        return Response(player_object, status=status.HTTP_200_OK)


class PlayerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    logger = logging.getLogger(__name__)

    def get(self, request, player_id=None):
        try:
            user_role = User_Role.objects.get(user_id=request.user.id)
        except User_Role.DoesNotExist:
            message = "Invalid user id"
            self.logger.debug("Invalid user id")
            raise UserDoesNotExistException("400", message, "user role does not exist")
        if user_role.role.type == 'P':
            message = "User does not have access"
            self.logger.debug(f"User does not have access")
            raise RoleDoesNotHaveAccessException("403", "Permission Denied", message)
        players = Player.objects.all()
        page = request.GET.get("page")
        players_paginated = populate_pagination(page, players)
        player_serializer = PlayerListSerializer(players_paginated, many=True)
        player_list = []
        for player in player_serializer.data:
            player_object = {
                'id': player['id'],
                'full_name': player['user']['first_name'] + ' ' + player['user']['last_name'],
                'team': player['team']['name']
            }
            player_list.append(player_object)
        return Response(player_list, status=status.HTTP_200_OK)
