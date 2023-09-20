from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('wins', views.wins, name='wins'),
    path('sales', views.sales, name='sales')
]
