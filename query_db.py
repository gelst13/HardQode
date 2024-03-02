# python manage.py shell
# import query_db
# query_db.check_start()
# query_db.drop()
# query_db.run()
# query_db.status()
# from edu.models import Product
# from edu.models import Lesson
# Lesson.objects.all()
# p = Product.objects.first()
# l = Lesson.objects.first()
# l.course
#

from django.contrib.auth.models import User
from edu.models import Product, Team
from users.models import Profile
import datetime
import pytz


def drop():
    # User.objects.get(username='User3').delete()
    # Team.objects.first().delete()
    # t = Team.objects.all()
    pass


def status():
    teams = Team.objects.all()
    for team in teams:
        students = Profile.objects.filter(team=team).all()
        print(f'В группу {team.name} набрано {len(students)} человек')
        for student in students:
            print(student.team.name, student.user)


def start_team(product):
    name = product.author[:1] + product.title[:1] + '00'
    print(f'start team {name}')
    t1 = Team(course=product, name=name)
    t1.save()
    return t1


def reformat_teams(product_students: dict, product):
    n = len(product_students.keys()) - 2
    new_name = product_students['cluster'] + str(n)
    new_team = Team(course=product, name=new_name)
    new_team.save()
    print(new_team.name)
    for team_name, team_students in product_students.items():
        if team_name.endswith(str(n-1)):
            for i in range(product.min_users):
                student = team_students[i]
                student.team = new_team
                student.save()
            return new_team


def check_teams(product):
    existing_teams = Team.objects.filter(course=product)
    print(existing_teams)
    if not existing_teams:
        start = start_team(product)
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
    if check_start(product):  # course_has_not_started_yet
        new_team = reformat_teams(product_students, product)
        return new_team
    else:
        print('Извините, набор в группы на данный курс уже закрыт.')
        return None


def run():
    product = Product.objects.get(id=1)
    for i in range(9, 10):
        new_user_name = 'User' + str(i)
        print()
        new_user = User(username=new_user_name)
        new_user.save()
        print(new_user.username)
        course_was_paid_for = True
        if course_was_paid_for:
            available_team = check_teams(product)
            print(f'available_team {available_team.name}')
            if available_team:
                new_user_profile = Profile.objects.get(user=new_user)
                new_user_profile.team = available_team
                new_user_profile.save()
                print(f'{new_user.username} зачислен в группу {Profile.objects.get(user=new_user).team.name}')
    status()


def check_start(product):
    # course_has_not_started_yet
    utcnow = datetime.datetime.now(tz=pytz.utc)
    return utcnow < product.start_date_time
