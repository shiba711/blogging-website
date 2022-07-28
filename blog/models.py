from email.quoprimime import body_check
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    thumbnail =models.URLField()
    reads = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

