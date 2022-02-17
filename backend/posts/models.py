from django.db import models

from django.contrib.auth.models import User
from groups.models import Group

from datetime import datetime


# the route of the file
def nameFile(instance, filename):
    return '/'.join(['img', str(instance.posted_by), str(instance.title), filename])



# Create your models here.

# here we will be able to upload the memes as images via the django rest framework

class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField(default="")
    meme =models.ImageField(upload_to=nameFile, blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(blank=True, default=datetime.now)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    
    
class SubComment(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(blank=True, default=datetime.now)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
