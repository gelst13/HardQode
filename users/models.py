from django.db import models
from django.contrib.auth.models import User
from edu.models import Team, Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} профиль'
    
    @property
    def course(self):
        if self.team:
            return self.team.course
        else:
            return None
