from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from .models import User, Exercise
from .forms import ExerciseForm

#from .forms import CategoryForm, WorkoutForm, ExerciseForm


def registration(request): 
    return render(request, "registration.html")

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def workout(request):
    return render(request, "workout.html")

def administrator(request):
    showall = Exercise.objects.all()
    return render(request, "admin.html", {"data":showall})

"""def exercise(request):
    if request.method=="POST":
        if request.POST.get('exercise_name') and request.POST.get('duration') and request.POST.get('description') and request.POST.get('video_url') and request.POST.get('workout'):
            saverecord = Exercise()
            saverecord.exercise_name = request.POST.get('exercise_name')
            saverecord.duration = request.POST.get('duration')
            saverecord.description = request.POST.get('description')
            saverecord.video_url = request.POST.get('video_url')
            saverecord.workout = request.POST.get('workout')
            saverecord.save()
            messages.success(request, "Exercise "+saverecord.exercise_name+" saved successfully")
            return render(request, "exercise.html")
    else:
            return render(request, "exercise.html")"""
        
def exercise_list(request):
    return render(request, "exercises/exercise_list.html")

def exercise_form(request):
    form = ExerciseForm()
    return render(request, "exercises/exercise_form.html", {'form':form})

def exercise_delete(request):
    return
