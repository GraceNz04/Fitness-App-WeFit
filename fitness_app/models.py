from django.db import models
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=40)
    weight = models.FloatField()
    height = models.FloatField()
    password = models.CharField(max_length=255, default='1234')
    def clean(self) -> None:
        today = datetime.date.today()
        if self.dob == today:
            raise ValidationError("Your birth date can not be today!")
        elif self.dob > today:
            raise ValidationError('Your birth date is impossible!')
        return super().clean()
    
    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super().save(*args, **kwargs)


        
class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=400)  

class Workout(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='workouts')

class Exercise(models.Model):
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    video_url = models.URLField(default='https://example.com/default-video-url')
    description = models.TextField(blank=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    

class UserExercise(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Exercise, on_delete=models.CASCADE)






