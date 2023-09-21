from django.shortcuts import render
from .models import Artist


def wins_main(request):
    return render(request, 'wins/wins.html')


def wins_male(request):
    artists = Artist.objects.order_by('name')
    return render(request, 'wins/male.html', {'artists': artists})


def wins_female(request):
    return render(request, 'wins/female.html')
