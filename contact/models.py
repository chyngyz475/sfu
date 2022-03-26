from unicodedata import name
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=70)
    courses = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    subject = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name
