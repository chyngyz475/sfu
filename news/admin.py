from csv import list_dialects
from django.contrib import admin
from.models import News, Comment,Tag
from .import models


class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "create_at", "id"]



# Register your models here.
admin.site.register(models.News,)
admin.site.register(models.Comment)
admin.site.register(models.Tag)


