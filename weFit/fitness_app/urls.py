from django.urls import path, include

from . import views

# Namespacing:
# app_name = main
urlpatterns = [
    # ex. /main/
    #path("", views.index, name="index"),
    # ex. /main/students/
    path("registration/", views.registration, name='registration'),
    path("login/", views.login, name='login'),
    path("home/", views.home, name="home"),
]