from django.shortcuts import render


def wins_main(request):
    return render(request, 'wins/wins.html')


def wins_male(request):
    return render(request, 'wins/male.html')


def wins_female(request):
    return render(request, 'wins/female.html')
