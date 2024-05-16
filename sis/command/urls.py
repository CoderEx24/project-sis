from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'command'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', LoginView.as_view(template_name='command/login.html'), name='index'),
    path('logout', views.logout, name='logout'),
    path('students', views.students, name='students'),
    path('professors', views.professors, name='profs'),
    path('ta', views.teaching_assistants, name='ta'),
    path('courses', views.courses, name='courses'),
    path('courses/withdraw', views.withdraw_course, name='withdraw_course'),
    path('courses/create', views.create_course, name='create_course'),
    path('report', views.report, name='report'),
]

