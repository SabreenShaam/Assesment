import logging

from django.db.models import Avg
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from bbms.exceptions import RoleDoesNotHaveAccessException, CoachDoesNotExistException, UserDoesNotExistException
from bbms.models import User_Role, Coach, Player, Team_Stat
from bbms.serializers.coach_serializer import CoachSerializer
from bbms.serializers.player_serializer import PlayerListSerializer


class CoachApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    logger = logging.getLogger(__name__)

    def get(self, request, coach_id=None):
        try:
            user_role = User_Role.objects.get(user_id=request.user.id)
        except User_Role.DoesNotExist:
            message = "Invalid user id"
            self.logger.debug("Invalid user id")
            raise UserDoesNotExistException("400", message, "user role does not exist")
        if user_role.role.type != 'C':
            message = "User does not have access"
            self.logger.debug(f"User does not have access")
            raise RoleDoesNotHaveAccessException("403", "Permission Denied", message)
        coach = Coach.objects.filter(id=coach_id).first()
        if coach is None:
            message = "Invalid coach_id"
            self.logger.debug(f"Invalid coach_id: {coach_id}")
            raise CoachDoesNotExistException("400", "Coach does not exist", message)
        coach_serializer = CoachSerializer(instance=coach).data
        team_id = coach_serializer['team']['id']
        team_name = coach_serializer['team']['name']
        players = Player.objects.filter(team_id=team_id)
        player_serializer = PlayerListSerializer(players, many=True)
        player_list = []
        for player in player_serializer.data:
            player_object = {'id': player['id'], 'name': player['user']['first_name'] + ' ' + player['user']['last_name']}
            player_list.append(player_object)
        team_details = {
            'team_name': team_name,
            'average_team_score': Team_Stat.objects.filter(team_id=team_id).aggregate(Avg('score'))['score__avg'],
            'players': player_list,
        }
        return Response(team_details, status=status.HTTP_200_OK)
