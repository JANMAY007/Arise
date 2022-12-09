from django.urls import path
from . import views

app_name = 'opening'

urlpatterns = [
    path('', views.all_openings, name="Openings"),
    path('<int:openings_id>/', views.opening, name="Temporary"),
]
