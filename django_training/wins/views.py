from django.shortcuts import render, get_object_or_404
from .models import Artist


def wins_main(request):
    return render(request, 'wins/wins.html')


def wins_artists(request, gender):
    artists = Artist.objects.filter(gender=gender).order_by('name')
    return render(request, 'wins/artists_list.html', {'artists': artists})


def artist_detail(request, gender, artist_slug):
    artist = get_object_or_404(Artist, slug=artist_slug)

    return render(request, 'wins/artist_wins.html', {'artist': artist})
