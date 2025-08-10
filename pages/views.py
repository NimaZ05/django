from django.shortcuts import render 
from django.views import View
from django.http import HttpResponse


def home_view(request):
    return render(request, 'pages/index.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')