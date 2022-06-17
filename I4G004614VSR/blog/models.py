from cgitb import text
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField(default = datetime.today)
    Published_date = models.DateTimeField(default = datetime.today)