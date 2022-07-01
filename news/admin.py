from csv import list_dialects
from django.contrib import admin
from.models import Blog
from .import models


class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "create_at", "id"]



# Register your models here.
admin.site.register(models.Blog)



