from django.db import models


# Create your models here.
class Group(models.Model):
    group_name = models.CharField(unique=True, max_length=120)
    followers_number = models.IntegerField()
    
    def __str__(self):
        return self.group_name