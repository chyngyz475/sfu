from csv import list_dialects
from django.contrib import admin
from.models import News, Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "create_at", "id"]



# Register your models here.
admin.site.register(News)
admin.site.register(Post)
admin.site.register(Comment)


