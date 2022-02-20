from django.db import models

# import the user model
from django.contrib.auth.models import User, AbstractUser

class Profile(User):
    
    def __str__(self):
        return self.username
        