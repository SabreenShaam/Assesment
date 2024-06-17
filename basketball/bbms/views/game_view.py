import logging

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from bbms.exceptions import UserDoesNotExistException
from bbms.models import Game, User_Role
from bbms.serializers.game_serializer import GameSerializer
from bbms.serializers.user_role_serializer import UserRoleSerializer


class ScoreCardApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    logger = logging.getLogger(__name__)

    def get(self, request):
        try:
            user_role = User_Role.objects.get(user_id=request.user.id)
        except User_Role.DoesNotExist:
            message = "Invalid user id"
            self.logger.debug("Invalid user id")
            raise UserDoesNotExistException("400", message, "user role does not exist")
        scores = Game.objects.all()
        game_serializer = GameSerializer(scores, many=True)
        user_serializer = UserRoleSerializer(instance=user_role).data
        self.logger.debug("scorecard get method called")
        scorecard = {
            "game": game_serializer.data,
            "user": user_serializer
        }
        return Response(scorecard, status=status.HTTP_200_OK)
