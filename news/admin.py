from csv import list_dialects
from django.contrib import admin
from.models import News, Post, Comment,Category,Tag
from mptt.admin import MPTTModelAdmin
from .import models


class PostAdmin(admin.ModelAdmin):
    list_display = ["name","category", "create_at", "id"]



# Register your models here.
admin.site.register(models.News, MPTTModelAdmin)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Category)
admin.site.register(models.Tag)


