from django.shortcuts import render
from .models import Feedback


def index(request):
    return render(request, 'addition.html')


def about(request):

    return render(request, 'about_me.html')

