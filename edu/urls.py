from django.urls import path
from . import views
from .views import CourseDetailView, VideoListView


urlpatterns = [
    path('', views.home, name='edu-home'),
    # path('', ProductListView.as_view(), name='edu-home'),
    path('about/', views.about, name='edu-about'),
    # path('course/<int:pk>', views.course_detail, name='course-detail'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('course/<int:pk>/buy', views.buy_course, name='buy-course'),
    path('course/<int:pk>/video', VideoListView.as_view(), name='course-video'),
]
