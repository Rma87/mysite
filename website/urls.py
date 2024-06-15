
from django.urls import path
from website.views import *

app_name = "website"

urlpatterns = [
    path('',home_page, name='index'),
    path('about/',about_page, name='about'),
    path('contact/',contact_page, name='contact'),
    path('elements/',elements_page, name='elements'),
]