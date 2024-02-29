from django.db import models
from datetime import datetime
from zoneinfo import ZoneInfo
import pytz


class Product(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    start_date_time = models.DateTimeField()
    price = models.FloatField()
    min_users = models.IntegerField()
    max_users = models.IntegerField()

    def __str__(self):
        return self.title
    
    @property
    def date_msk(self):
        return self.start_date_time.astimezone(ZoneInfo("Europe/Moscow")).strftime('%d.%m.%Y %H:%M %z%Z')


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200)
    course = models.ForeignKey(Product, on_delete=models.CASCADE)
    

