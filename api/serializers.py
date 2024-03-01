from rest_framework import serializers
from edu.models import Product, Lesson


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['author', 'title', 'date_msk', 'price', 'min_users', 'max_users', 'number_of_lessons']


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_link', 'course']
