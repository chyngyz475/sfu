from optparse import Option
from re import T
import time
from turtle import title
from venv import create
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
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

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
      author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
      title = models.CharField(max_length=200)
      image = models.ImageField(upload_to='articles/')
      text = models.TextField()
      category = models.ForeignKey(
            Category,
            related_name="post",
            on_delete=models.SET_NULL,
            null=True 
            )
      create_at = models.DateTimeField(auto_now_add=True)
      
class Comment(models.Model):
       name = models.CharField(max_length=50)
       email = models.CharField(max_length=150)
       website = models.CharField(max_length=150, blank=True, null=True )
       message = models.TextField(max_length=500)
       create_at = models.DateTimeField(auto_now_add=True)
       post = models.ForeignKey(
             Post,
             related_name="comment",
             on_delete=models.CASCADE,
             null=True,
             blank=True
       )
       
