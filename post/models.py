from tkinter import CASCADE
from django.db import models

# Create your models here.



from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    last_update=models.DateTimeField(auto_now_add=True,blank=True)
    desciption=models.TextField()
    


class Comment(models.Model):
    user_comment=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_given=models.TextField()
