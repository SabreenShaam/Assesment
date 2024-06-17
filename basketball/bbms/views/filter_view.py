import logging

from django.db.models import Sum, Avg
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from bbms.exceptions import PlayerDoesNotExistException, RoleDoesNotHaveAccessException, UserDoesNotExistException
from bbms.helper import calculate_percentile
from bbms.models import User_Role, Player, Player_Stat, Team_Stat
from bbms.serializers.player_serializer import PlayerListSerializer


class FilterPlayerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    logger = logging.getLogger(__name__)

    def get(self, request, player_id=None):
        try:
            user_role = User_Role.objects.get(user_id=request.user.id)
        except User_Role.DoesNotExist:
            message = "Invalid user id"
            self.logger.debug("Invalid user id")
            raise UserDoesNotExistException("400", message, "user role does not exist")
        if user_role.role.type == 'C':
            player = Player.objects.filter(id=player_id).first()

            if player is None:
                message = "Invalid player id"
                self.logger.debug(f"Invalid player id: {player_id}")
                raise PlayerDoesNotExistException("400", "Player does not exist", message)
            total_player_Score = Player_Stat.objects.filter(player_id=player_id).aggregate(Sum('score'))['score__sum']
            if total_player_Score is None:
                message = "The Player in bench"
                self.logger.debug(f"The player did not participate any games: {player_id}")
                raise PlayerDoesNotExistException("400", "The player did not participate in any games", message)
            game_ids = list(Player_Stat.objects.filter(player_id=player_id).values('game_id'))
            game_id_list = [x['game_id'] for x in game_ids]
            total_team_Score = Team_Stat.objects.filter(team_id=player.team.id, game_id__in=game_id_list).aggregate(Sum('score'))['score__sum']
            player_score_percentage_across_team = total_player_Score / total_team_Score * 100
            player_object = {
                'id': player.id,
                'full_name': player.user.first_name + ' ' + player.user.last_name,
                'team': player.team.name,
                'score_percentage': player_score_percentage_across_team
            }
            return Response(player_object, status=status.HTTP_200_OK)
        else:
            message = "User does not have access"
            self.logger.debug(f"User does not have access")
            raise RoleDoesNotHaveAccessException("403", "Permission Denied", message)


class FilterTeamApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    logger = logging.getLogger(__name__)

    def get(self, request, team_id=None):
        try:
            user_role = User_Role.objects.get(user_id=request.user.id)
        except User_Role.DoesNotExist:
            message = "Invalid user id"
            self.logger.debug("Invalid user id")
            raise UserDoesNotExistException("400", message, "user role does not exist")
        if user_role.role.type == 'C':
            players = Player.objects.filter(team_id=team_id)
            if len(list(players)) == 0:
                message = "Invalid team id"
                self.logger.debug(f"Invalid team id: {team_id}")
                raise PlayerDoesNotExistException("400", "Players does not exist", message)
            player_serializer = PlayerListSerializer(players, many=True)
            player_avg_score_list = []
            player_avg_score_object_list = []
            for player in player_serializer.data:
                plyer_object = {}
                player_avg_score = Player_Stat.objects.filter(player_id=player['id']).aggregate(Avg('score'))[
                    'score__avg']
                player_avg_score_list.append(player_avg_score)
                plyer_object['name'] = player['user']['first_name'] + ' ' + player['user']['last_name']
                plyer_object['avg_ninety_percentile_score'] = player_avg_score
                plyer_object['id'] = player['id']
                player_avg_score_object_list.append(plyer_object)
            percentile = calculate_percentile(player_avg_score_list)
            percentile_object = {}
            for player_score_object in player_avg_score_object_list:
                if player_score_object['avg_ninety_percentile_score'] == percentile:
                    percentile_object = player_score_object
                    break
            return Response(percentile_object, status=status.HTTP_200_OK)
        else:
            message = "User does not have access"
            self.logger.debug(f"User does not have access")
            raise RoleDoesNotHaveAccessException("403", "Permission Denied", message)
