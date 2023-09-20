from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


# def wins(request):
#     return render(request, 'main/wins.html')


def sales(request):
    return render(request, 'main/sales.html')
