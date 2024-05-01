from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'website/home.html')

def about_page(request):
    return render(request, 'website/about.html')
