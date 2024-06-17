from rest_framework import status
from basketball.exceptions import BaseBasketBallApiException


class UserDoesNotExistException(BaseBasketBallApiException):
    status_code = status.HTTP_403_FORBIDDEN


class PlayerDoesNotExistException(BaseBasketBallApiException):
    status_code = status.HTTP_400_BAD_REQUEST


class CoachDoesNotExistException(BaseBasketBallApiException):
    status_code = status.HTTP_400_BAD_REQUEST


class RoleDoesNotHaveAccessException(BaseBasketBallApiException):
    status_code = status.HTTP_403_FORBIDDEN


class TeamDoesNotExistException(BaseBasketBallApiException):
    status_code = status.HTTP_403_FORBIDDEN


