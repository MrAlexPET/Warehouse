from django.urls import path
from . import views

urlpatterns = [
    path('', views.wins_main, name='wins_main'),
    path('male/', views.wins_male, name='wins_male'),
    path('female/', views.wins_female, name='wins_female')
]
