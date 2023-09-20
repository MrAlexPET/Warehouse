from django.shortcuts import render


def wins_main(request):
    return render(request, 'wins/wins.html')
