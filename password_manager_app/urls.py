from django.contrib import admin
from django.urls import path, include
from password_manager_app.views import Index,logged_in,login,register,logout
import random
from random import randint
import string


def get_random_string():
    result_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(50,60))])
    return result_str


urlpatterns = [
    path('', Index,name='home'),
    path('personalArea', logged_in,name="personalArea"),
    path('login', login,name='login'),
    path('register', register,name='register'),
    path('logout', logout,name='logout'),
]
