from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    LessonDetailView,
    EnrollCourseView,
    MyCourseListView,
)

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('meus-cursos/', MyCourseListView.as_view(), name='my_courses'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('<slug:course_slug>/aula/<int:lesson_id>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('<slug:slug>/matricular/', EnrollCourseView.as_view(), name='enroll_course'),
]
