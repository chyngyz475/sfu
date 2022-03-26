import time
from turtle import title
from venv import create
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class News(models.Model):
   title = models.CharField(max_length=250)
   cteated_at = models.DateField(auto_now_add=True)
   photo = models.ImageField(upload_to='%Y/%m/%d')
   content = models.TextField(max_length=500)
   
   
   def __str__(self):
      return


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

