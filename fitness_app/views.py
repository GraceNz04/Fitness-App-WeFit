from django.http import HttpResponse
from django.shortcuts import render

from .models import User, Exercise

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Workout, Exercise
from .forms import CategoryForm, WorkoutForm, ExerciseForm

def registration(request): 
    return render(request, "registration.html")

def arms_workouts(request):
    return render(request, 'ArmsAndBackWorkouts/armsworkouts.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'ArmsAndBackWorkouts/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'ArmsAndBackWorkouts/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'ArmsAndBackWorkouts/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('ArmsAndBackWorkouts/category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'ArmsAndBackWorkouts/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('ArmsAndBackWorkouts/category_list')
    return render(request, 'ArmsAndBackWorkouts/category_confirm_delete.html', {'category': category})

# Workout views
def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'ArmsAndBackWorkouts/workout_list.html', {'workouts': workouts})

def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'ArmsAndBackWorkouts/workout_detail.html', {'workout': workout})

def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ArmsAndBackWorkouts/workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'ArmsAndBackWorkouts/workout_form.html', {'form': form})

def workout_update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('ArmsAndBackWorkouts/workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'ArmsAndBackWorkouts/workout_form.html', {'form': form})

def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('ArmsAndBackWorkouts/workout_list')
    return render(request, 'ArmsAndBackWorkouts/workout_confirm_delete.html', {'workout': workout})

# Exercise views
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'ArmsAndBackWorkouts/exercise_list.html', {'exercises': exercises})

def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'ArmsAndBackWorkouts/exercise_detail.html', {'exercise': exercise})

def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ArmsAndBackWorkouts/exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'ArmsAndBackWorkouts/exercise_form.html', {'form': form})

def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('ArmsAndBackWorkouts/exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'ArmsAndBackWorkouts/exercise_form.html', {'form': form})

def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('ArmsAndBackWorkouts/exercise_list')
    return render(request, 'ArmsAndBackWorkouts/exercise_confirm_delete.html', {'exercise': exercise})