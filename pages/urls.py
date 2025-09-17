from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', home_view, name="index"),
    path('about', about_view, name="about"),
    path('contact', contact_view, name="contact"),
    path('newsletter', newsletter_view, name="newsletter"),
    path('test', test, name="test")
]
