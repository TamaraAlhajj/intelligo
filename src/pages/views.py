from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html", {})


def info(request):
    return render(request, "info.html", {})


def bigO(request):
    return render(request, "bigO.html", {})


def masters(request):
    return render(request, "masters.html", {})
