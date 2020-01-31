from django.shortcuts import render


def about(request):
    return render(request, 'base/about.html')


def user(request):
    return render(request, 'base/user.html')
