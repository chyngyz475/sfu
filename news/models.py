import time
from turtle import title
from venv import create
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class News(models.Model):
    image = models.ImageField(upload_to='portfolio/images/', height_field=None , width_field=None)
    title = models.CharField(max_length=100)
    date  = models.DateField()
    description = models.CharField(max_length=500)
    text = models.TextField(max_length=150000)
    
    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name



      
class Comment(models.Model):
       name = models.CharField(max_length=100)
       direction = models.CharField(max_length=100)
       email = models.CharField(max_length=150)
       contact = models.CharField(max_length=150, blank=True, null=True )
       message = models.TextField(max_length=500)
       
       def __str__(self):
           return self.name

