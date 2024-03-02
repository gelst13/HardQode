from rest_framework import permissions, viewsets
from .serializers import ProductSerializer, LessonSerializer
from edu.models import Product, Lesson


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('title')
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lessons to be viewed or edited.
    Реализовать API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [permissions.IsAuthenticated]

