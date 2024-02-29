from django.db import models
from django.utils import timezone


class Product(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    start_date_time = models.DateTimeField()
    price = models.FloatField()
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    
    # author = models.ForeignKey(User, on_delete=models.CASCADE)   # on_delete here is set so when user is deleted, so are his posts

    def __str__(self):
        return self.title


