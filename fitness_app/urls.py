from django.urls import path, include

from . import views

# Namespacing:
# app_name = main
urlpatterns = [
    # ex. /main/
    #path("", views.index, name="index"),
    # ex. /main/students/
    path("registration/", views.registration),
    
   path('ArmsAndBackWorkouts/armsworkouts/', views.arms_workouts, name='arms_workouts'),

   path('ArmsAndBackWorkouts/categories/', views.category_list, name='category_list'),
    path('ArmsAndBackWorkouts/categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('ArmsAndBackWorkouts/categories/create/', views.category_create, name='category_create'),
    path('ArmsAndBackWorkouts/categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('ArmsAndBackWorkouts/categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Workout URLs
    path('ArmsAndBackWorkouts/workouts/', views.workout_list, name='workout_list'),
    path('ArmsAndBackWorkouts/workouts/<int:pk>/', views.workout_detail, name='workout_detail'),
    path('ArmsAndBackWorkouts/workouts/create/', views.workout_create, name='workout_create'),
    path('ArmsAndBackWorkouts/workouts/<int:pk>/update/', views.workout_update, name='workout_update'),
    path('ArmsAndBackWorkouts/workouts/<int:pk>/delete/', views.workout_delete, name='workout_delete'),

    # Exercise URLs
    path('ArmsAndBackWorkouts/exercises/', views.exercise_list, name='exercise_list'),
    path('ArmsAndBackWorkouts/exercises/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('ArmsAndBackWorkouts/exercises/create/', views.exercise_create, name='exercise_create'),
    path('ArmsAndBackWorkouts/exercises/<int:pk>/update/', views.exercise_update, name='exercise_update'),
    path('ArmsAndBackWorkouts/exercises/<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
]