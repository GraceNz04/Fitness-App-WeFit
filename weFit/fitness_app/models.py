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
    dob = models.DateField()
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
    
class Exercise(models.Model):
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    duration = models.IntegerField(default=20)
    description = models.TextField(blank=True)
    demonstration = models.FileField()
    
class UserExercise(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Exercise, on_delete=models.CASCADE)
        
    

