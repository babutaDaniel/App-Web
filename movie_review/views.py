from django.shortcuts import render


def homepage_view(request):
    return render(request, 'homepage.html', {})






























def troll_view(request):
    return render(request, 'troll.html', {})

