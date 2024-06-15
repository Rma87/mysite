from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'website/index.html')

def about_page(request):
    return render(request, 'website/about.html')

def contact_page(request):
    return render(request, 'website/contact.html')

def elements_page(request):
    return render(request, 'website/elements.html')