from csv import list_dialects
from django.contrib import admin
from . import models 
# Register your models here.
@admin.register(models.Post)
class AplicationAdmin(admin.ModelAdmin):
    pass