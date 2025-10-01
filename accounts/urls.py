from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
]
