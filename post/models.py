from tkinter import CASCADE
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    last_update=models.DateTimeField(auto_now_add=True,null=True)
    description=models.TextField()


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField()


class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)






