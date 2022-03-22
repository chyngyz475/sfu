from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class NewPost(models.Model):
      author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
      title = models.CharField(max_length=200)
      image = models.ImageField(upload_to='articles/')
      text = models.TextField(max_length=500)
      create_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
      name = models.CharField(max_length=20),
      direction =models.CharField( max_length=100),
      contact = models.CharField(max_length=50),
      email = models.EmailField(max_length=100),
      message =models.CharField(max_length=300)
