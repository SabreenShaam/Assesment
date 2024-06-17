from django.urls import path

from bbms.views.coach_view import CoachApiView
from bbms.views.filter_view import FilterPlayerApiView, FilterTeamApiView
from bbms.views.game_view import ScoreCardApiView
from bbms.views.player_view import PlayerApiView, PlayerDetailApiView
from bbms.views.stats_view import StatsApiView
from bbms.views.team_view import TeamApiView, TeamDetailApiView

urlpatterns = [
    path('scorecard', ScoreCardApiView.as_view()),
    path('player', PlayerApiView.as_view()),
    path('player/<int:player_id>', PlayerDetailApiView.as_view()),
    path('coach/<int:coach_id>', CoachApiView.as_view()),
    path('team', TeamApiView.as_view()),
    path('team/<int:team_id>', TeamDetailApiView.as_view()),
    path('stats', StatsApiView.as_view()),
    path('filter/player/<int:player_id>', FilterPlayerApiView.as_view()),
    path('filter/team/<int:team_id>', FilterTeamApiView.as_view())
    ]
