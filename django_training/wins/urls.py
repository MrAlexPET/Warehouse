from django.urls import path
from . import views

urlpatterns = [
    path('', views.wins_main, name='wins_main')
]
