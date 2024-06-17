import logging

from django.db.models import Avg
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from bbms.exceptions import RoleDoesNotHaveAccessException, PlayerDoesNotExistException, UserDoesNotExistException
from bbms.helper import populate_pagination
from bbms.models import Team, User_Role, Player, Team_Stat
from bbms.serializers.player_serializer import PlayerListSerializer
from bbms.serializers.team_serializer import TeamSerializer


class TeamDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    logger = logging.getLogger(__name__)

    def get(self, request, team_id=None):
        try:
            user_role = User_Role.objects.get(user_id=request.user.id)
        except User_Role.DoesNotExist:
            message = "Invalid user id"
            self.logger.debug("Invalid user id")
            raise UserDoesNotExistException("400", message, "user role does not exist")
        if user_role.role.type != 'P':
            players = Player.objects.filter(team_id=team_id)
            if len(list(players)) == 0:
                message = "Invalid team id"
                self.logger.debug(f"Invalid team id: {team_id}")
                raise PlayerDoesNotExistException("400", "Players does not exist", message)
            player_serializer = PlayerListSerializer(players, many=True)
            context = {
                'players': player_serializer.data,
                'average_team_score': Team_Stat.objects.filter(team_id=team_id).aggregate(Avg('score'))['score__avg'],
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            message = "User does not have access"
            self.logger.debug(f"User does not have access")
            raise RoleDoesNotHaveAccessException("403", "Permission Denied", message)


class TeamApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    logger = logging.getLogger(__name__)

    def get(self, request):
        try:
            user_role = User_Role.objects.get(user_id=request.user.id)
        except User_Role.DoesNotExist:
            message = "Invalid user id"
            self.logger.debug("Invalid user id")
            raise UserDoesNotExistException("400", message, "user role does not exist")
        if user_role.role.type == 'A':
            teams = Team.objects.all()
            page = request.GET.get("page")
            teams_paginated = populate_pagination(page, teams)
            player_serializer = TeamSerializer(teams_paginated, many=True)
            return Response(player_serializer.data, status=status.HTTP_200_OK)
        else:
            message = "User does not have access"
            self.logger.debug(f"User does not have access")
            raise RoleDoesNotHaveAccessException("403", "Permission Denied", message)
