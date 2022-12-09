from django.urls import path
from . import views


app_name = 'examination'

urlpatterns = [
    path('', views.all_exams, name='all_exams'),
]
