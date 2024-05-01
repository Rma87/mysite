from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h1>this is a Home page<h1>')

def about_page(request):
    return HttpResponse('<h1>this is a About page<h1>')
