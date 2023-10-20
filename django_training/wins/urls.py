from django.urls import path
from . import views

urlpatterns = [
    path('', views.wins_main, name='wins_main'),
    path('<str:gender>/', views.wins_artists, name='wins_artists'),
    path('<str:gender>/<slug:artist_slug>/', views.artist_detail, name='artist_detail'),
]
