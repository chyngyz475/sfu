from turtle import title
from venv import create
from django.db import models

class News(models.Model):
   title = models.CharField(max_length=250)
   content = models.TextField(max_length=500)
   cteated_at = models.DateField(auto_now_add=True)
   photo = models.ImageField(upload_to='%Y/%m/%d')
   
   
   def __str__(self):
      return

class Post(models.Model):
      title = models.CharField(max_length=200)
      image = models.ImageField(upload_to='articles/')
      text = models.TextField()
      create_at = models.DateTimeField(auto_now_add=True)
      
class Comment(models.Model):
       name = models.CharField(max_length=50)
       email = models.CharField(max_length=150)
       website = models.CharField(max_length=150)
       message = models.TextField(max_length=500)
       
