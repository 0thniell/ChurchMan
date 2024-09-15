from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # user app url
    # path('', views.home, name='home'),
    # path('home', views.home, name='home'),
    path('sign-up', signup, name='signup'),
    # path('create-post', views.create_post, name='create-post'),
]

