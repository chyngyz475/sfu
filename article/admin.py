from atexit import register
from django.contrib import admin

from article import models

# Register your models here.
admin.site.register(models.Article)