from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import *
import datetime

# Create your tests here.

class UserModelTest(TestCase):
    def user_dob_equals_current_date(self):
        today = datetime.date.today()
        user = User(username='Test user1', email='myemail@mail.com',gender='male', weight='89', height='170', dob=today)
        self.assertRaises(ValidationError, user.save)
        
    def user_dob_greater_than_current_date(self):
        user = User(username='Test user2', dob='2030-06-04')
        self.assertRaises(ValidationError, user.save)


    
