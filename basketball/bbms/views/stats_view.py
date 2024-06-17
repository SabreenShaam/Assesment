import logging
from datetime import timedelta
from django.db.models import ExpressionWrapper, fields, Sum, Count, F
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from bbms.exceptions import RoleDoesNotHaveAccessException, UserDoesNotExistException
from bbms.models import User_Role, User_Stat


class StatsApiView(APIView):
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
            duration = ExpressionWrapper(F('logout_time') - F('login_time'), output_field=fields.DurationField())
            stats = User_Stat.objects.values('user_id').annotate(duration=Sum(duration)).annotate(
                dcount=Count('user_id')).filter(duration__gt=timedelta(seconds=2)).order_by('user_id')
            user_stats = {
                'stats': stats,
                'online_users_count': User_Role.objects.filter(is_logged_in=True).aggregate(Count('id'))['id__count'],
                'online_users': User_Role.objects.filter(is_logged_in=True).values_list('user_id', flat=True),
            }
            return Response(user_stats, status=status.HTTP_200_OK)
        else:
            message = "User does not have access"
            self.logger.debug(f"User does not have access")
            raise RoleDoesNotHaveAccessException("403", "Permission Denied", message)
