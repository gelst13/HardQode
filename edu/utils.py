from django.contrib.auth.models import User
from .models import Product, Team
from users.models import Profile
import datetime
import pytz


class EduSys:
    def __init__(self):
        self.n = 0
    
    @staticmethod
    def check_start(product):
        # course_has_not_started_yet
        utcnow = datetime.datetime.now(tz=pytz.utc)
        return utcnow < product.start_date_time
    
    @staticmethod
    def start_team(product):
        name = product.author[:1] + product.title[:1] + '00'
        print(f'start team {name}')
        t1 = Team(course=product, name=name)
        t1.save()
        return t1
    
    @staticmethod
    def reformat_teams(product_students: dict, product):
        n = len(product_students.keys()) - 2
        new_name = product_students['cluster'] + str(n)
        new_team = Team(course=product, name=new_name)
        new_team.save()
        print(new_team.name)
        for team_name, team_students in product_students.items():
            if team_name.endswith(str(n - 1)):
                for i in range(product.min_users):
                    student = team_students[i]
                    student.team = new_team
                    student.save()
                return new_team
    
    @staticmethod
    def reformat_teams(product_students: dict, product):
        n = len(product_students.keys()) - 2
        new_name = product_students['cluster'] + str(n)
        new_team = Team(course=product, name=new_name)
        new_team.save()
        print(new_team.name)
        for team_name, team_students in product_students.items():
            if team_name.endswith(str(n - 1)):
                for i in range(product.min_users):
                    student = team_students[i]
                    student.team = new_team
                    student.save()
                return new_team
    
    @staticmethod
    def check_teams(product):
        existing_teams = Team.objects.filter(course=product)
        print(existing_teams)
        if not existing_teams:
            start = EduSys.start_team(product)
            return start
        product_students = {'product_population': 0, 'cluster': product.author[:1] + product.title[:1] + '0'}
        for team in existing_teams:
            team_students = Profile.objects.filter(team=team).all()
            product_students.update({team.name: team_students})
            team_population = len(team_students)
            product_students['product_population'] += team_population
            print(f'Сейчас наполнение группы {team.name}: {team_population} из {product.max_users}')
            if team_population < product.max_users:
                return team
        if EduSys.check_start(product):  # course_has_not_started_yet
            new_team = EduSys.reformat_teams(product_students, product)
            return new_team
        else:
            print('Извините, набор в группы на данный курс уже закрыт.')
            return None
    
    @staticmethod
    def enroll_on_course(product_id: int, user_id: int):
        product = Product.objects.get(id=product_id)
        user = User.objects.get(id=user_id)
        available_team = EduSys.check_teams(product)
        print(f'available_team {available_team.name}')
        if available_team:
            user_profile = Profile.objects.get(user=user)
            user_profile.team = available_team
            user_profile.save()
            print(f'{user.username} зачислен в группу {Profile.objects.get(user=user).team.name}')
    
        

