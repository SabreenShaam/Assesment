import pytest
from django.contrib.auth.models import User
from rest_framework import status


@pytest.mark.django_db
def test_scorecard_with_valid_user(api_client, load_mock_data):
    user = User.objects.get(id=1)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/scorecard')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_player_list_with_non_player_role(api_client, load_mock_data):
    user = User.objects.get(id=161)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/player')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_player_list_with_player_role(api_client, load_mock_data):
    user = User.objects.get(id=1)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/player')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_player_detail_with_player_role(api_client, load_mock_data):
    user = User.objects.get(id=1)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/player/1')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_player_detail_with_non_player(api_client, load_mock_data):
    user = User.objects.get(id=161)
    api_client.force_authenticate(user=user)
    player_id = 1
    response = api_client.get(f'/player/{player_id}')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_team_belong_to_coach(api_client, load_mock_data):
    user = User.objects.get(id=161)
    api_client.force_authenticate(user=user)
    coach_id = 1
    response = api_client.get(f'/coach/{coach_id}')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_team_belong_to_coach_with_non_coach_role(api_client, load_mock_data):
    user = User.objects.get(id=1)
    api_client.force_authenticate(user=user)
    coach_id = 1
    response = api_client.get(f'/coach/{coach_id}')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_team_belong_to_coach_with_invalid_coach_id(api_client, load_mock_data):
    user = User.objects.get(id=1)
    api_client.force_authenticate(user=user)
    coach_id = 13
    response = api_client.get(f'/coach/{coach_id}')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_team_list_with_valid_role(api_client, load_mock_data):
    user = User.objects.get(id=177)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/team')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_team_list_with_invalid_role(api_client, load_mock_data):
    user = User.objects.get(id=171)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/team')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_team_detail_with_player_role(api_client, load_mock_data):
    user = User.objects.get(id=1)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/team/1')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_team_detail_with_non_player_role(api_client, load_mock_data):
    user = User.objects.get(id=162)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/team/1')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_stats_with_non_admin_role(api_client, load_mock_data):
    user = User.objects.get(id=1)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/stats')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_stats_with_admin_role(api_client, load_mock_data):
    user = User.objects.get(id=177)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/stats')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_filter_player_percentage_with_coach_role(api_client, load_mock_data):
    user = User.objects.get(id=162)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/filter/player/1')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_filter_player_percentage_with_non_coach_role(api_client, load_mock_data):
    user = User.objects.get(id=21)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/filter/player/1')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_filter_team_player_percentile_with_coach_role(api_client, load_mock_data):
    user = User.objects.get(id=162)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/filter/team/1')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_filter_team_player_percentile_with_non_coach_role(api_client, load_mock_data):
    user = User.objects.get(id=21)
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/filter/team/1')
    assert response.status_code == status.HTTP_403_FORBIDDEN
