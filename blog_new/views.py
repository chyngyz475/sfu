from django.shortcuts import render
from requests import request,render
from .models import Blog
# Create your views here.
def Blog(request):
    blog = Blog.objects.all()
    return render(request,'', {'blog':blog})