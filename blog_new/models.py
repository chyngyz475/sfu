from django.db import models
from django.db import models

# Create your models here.
class Blog(models.Model):
  url_height=models.PositiveIntegerField()
  url_width=models.PositiveIntegerField()
  title = models.CharField(max_length=250)
  image = models.ImageField()
  date = models.DateField()
  content = models.TextField(max_length=1000)