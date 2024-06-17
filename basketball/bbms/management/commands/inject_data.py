from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from bbms.models import Team, Role, User_Role, Coach, Player, Game, User_Stat, Team_Stat, Player_Stat
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from faker import Faker


class Command(BaseCommand):

    def add_team(self, fake):
        for t in range(16):
            try:
                team = Team(name=fake.slug())
            except ObjectDoesNotExist:
                raise CommandError('Team is not exist')
            team.save()
            self.stdout.write(
                self.style.SUCCESS('Team inserted successfully : "%s"' % team.name))

    def add_role(self):
        types = ['A', 'C', 'P']
        for type in range(len(types)):
            try:
                role = Role(type=types[type])
            except ObjectDoesNotExist:
                raise CommandError('Role is not exist')
            role.save()
            self.stdout.write(self.style.SUCCESS('Role inserted successfully "%s"' % role.type))

    def add_user(self, fake):
        for i in range(177):
            username = fake.user_name()
            password = 'password'
            try:
                if i == 176:
                    username = 'admin'
                user = User.objects.create_user(username=username + str(i+1), email=fake.safe_email(), password=password,
                                                first_name=fake.first_name(), last_name=fake.last_name())
            except ObjectDoesNotExist:
                raise CommandError('User is not exits')
            user.save()
            self.stdout.write(self.style.SUCCESS('User "%s" created successfully: "%s"' % (i, user.username)))

    def add_user_role(self, fake):
        users = User.objects.filter(is_superuser=False)

        admin = get_object_or_404(Role, type='A')
        coach = get_object_or_404(Role, type='C')
        player = get_object_or_404(Role, type='P')

        for user in users[:160]:
            try:
                p = User_Role(user_id=user.id, role_id=player.id, is_logged_in=fake.pybool())
            except ObjectDoesNotExist:
                raise CommandError('Error while adding user role')
            p.save()
            self.stdout.write(self.style.SUCCESS('player role added : { %s : %s }' % (user.username, player.type)))

        for user in users[160:176]:
            try:
                u = User_Role(user_id=user.id, role_id=coach.id, is_logged_in=fake.pybool())
            except coach.DoesNotExists:
                raise CommandError('Error while adding user')
            u.save()
            self.stdout.write(self.style.SUCCESS('coach role added : { %s : %s }' % (user.username, coach.type)))

        for user in users[176:]:
            try:
                u = User_Role(user_id=user.id, role_id=admin.id, is_logged_in=fake.pybool())
            except ObjectDoesNotExist:
                raise CommandError('Error while adding user role')
            u.save()
            self.stdout.write(self.style.SUCCESS('admin role added : { %s : %s }' % (user.username, admin.type)))

    def add_coach(self):
        teams = Team.objects.all()
        coach = Role.objects.filter(type='C').first()
        users = User_Role.objects.filter(role_id=coach.id)

        for i in range(len(teams)):
            try:
                coach = Coach(team_id=teams[i].id, user_id=users[i].user_id)
            except ObjectDoesNotExist:
                raise CommandError('Error while adding coach user')
            coach.save()
            self.stdout.write(self.style.SUCCESS('coach created  : %s ' % users[i].user_id))

    def add_player(self, fake):
        teams = Team.objects.all()
        player = Role.objects.filter(type='P').first()
        users = User_Role.objects.filter(role_id=player.id)

        total = 0
        for team in teams:
            counter = 0
            while counter < 10:
                try:
                    player = Player(team_id=team.id, user_id=users[total].user.id,
                                    height=fake.random_int(min=170, max=255, step=1))
                except ObjectDoesNotExist:
                    raise Warning('Error while adding player user')
                player.save()
                self.stdout.write(self.style.SUCCESS('player created  : %s %s' %
                                                     (users[total].user.first_name,
                                                      users[total].user.username)))
                total += 1
                counter += 1

    def add_qualifier_game(self, fake):
        teams = Team.objects.all()
        self.add_game(fake, teams, 'QF')

    def add_semifinal_game(self, fake):
        teams = Game.objects.filter(round_number='QF')
        self.add_game(fake, teams, 'SF')

    def add_final_game(self, fake):
        teams = Game.objects.filter(round_number='SF')
        self.add_game(fake, teams, 'FI')

    def add_winner(self, fake):
        teams = Game.objects.filter(round_number='FI')
        self.add_game(fake, teams, 'WI')

    def add_game(self, fake, teams, round_number):
        hosts = teams[1::2]
        guests = teams[0::2]

        for i in range(len(hosts)):
            host_score = fake.random_int(min=5, max=186, step=1)
            guest_score = fake.random_int(min=5, max=186, step=1)
            winner = hosts[i] if host_score > guest_score else guests[i]

            host_id = hosts[i].id if round_number == 'QF' else hosts[i].winner_id
            guest_id = guests[i].id if round_number == 'QF' else guests[i].winner_id
            winner_id = winner.id if round_number == 'QF' else winner.winner_id

            try:
                game = Game(host_id=host_id, guest_id=guest_id, host_score=host_score, guest_score=guest_score,
                            winner_id=winner_id, round_number=round_number,
                            date=fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None))
            except ObjectDoesNotExist:
                raise CommandError('Semifinal games added')
            game.save()
            self.stdout.write(self.style.SUCCESS('%s Game %s Vs %s =>  winner : %s '
                                                 % (round_number, host_id, guest_id, winner_id)))

    def add_user_stat(self, fake):
        users = User.objects.all()

        for user in users:
            for i in range(fake.random_int(min=1, max=10, step=1)):
                stat = User_Stat(user_id=user.id,
                                 login_time=fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),
                                 logout_time=fake.date_time_this_month(before_now=False, after_now=True, tzinfo=None)
                                 )
                stat.save()
                self.stdout.write(self.style.SUCCESS('User stat added  %s ' % user.id))

    def add_team_stat(self):
        teams = Team.objects.all()

        for team in teams:
            scores = Game.objects.filter( Q(host_id=team.id) | Q(guest_id=team.id) )
            for team_score in scores:
                team_id = team_score.host_id if team_score.host_id == team.id else team_score.guest_id
                game_score = team_score.host_score if team_score.host_id == team.id else team_score.guest_score
                host_stat = Team_Stat(score=game_score, game_id=team_score.id, team_id=team_id)
                host_stat.save()
                self.stdout.write(self.style.SUCCESS('Team stat added # %s ' % team_score.id))

    def add_player_stat(self):
        stats = Team_Stat.objects.all()

        for team_stat in stats:
            players = Player.objects.filter(team_id=team_stat.team_id).order_by('?')[:5]
            player_scores = self.generate_player_score(5, team_stat.score)

            for i in range(len(players)):
                player_stat = Player_Stat(score=player_scores[i], game_id=team_stat.game_id, player_id=players[i].id)
                player_stat.save()
                self.stdout.write(self.style.SUCCESS('Player stat added # %s : %s ' % (players[i].id, player_scores[i] )))

    def generate_player_score(self, n, total):
        import random
        dividers = sorted(random.sample(range(1, total), n - 1))
        return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

    def handle(self, *args, **options):
        fake = Faker()
        self.add_team(fake)
        self.add_role()
        self.add_user(fake)
        self.add_user_role(fake)
        self.add_user_stat(fake)
        self.add_coach()
        self.add_player(fake)
        self.add_qualifier_game(fake)
        self.add_semifinal_game(fake)
        self.add_final_game(fake)
        self.add_winner(fake)
        self.add_team_stat()
        self.add_player_stat()
