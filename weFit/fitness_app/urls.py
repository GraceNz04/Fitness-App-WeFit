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
    path("workout/", views.workout, name="workout"),
    path("exercise_list/", views.exercise_list, name="exercise_list"),
    path("exercise_form/", views.exercise_form, name='exercise_form')

]