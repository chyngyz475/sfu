from django.views.generic import ListView
import pdb
from django.shortcuts import render
from django.http import HttpResponse
from news.models import Post


def home(request):
    return render(request, 'base.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

def single(request):
    return render(request, 'single.html')

def blog(request):
    return render(request, 'blog.html')

def blog(request):
    return render(request, 'blog.html')

def admissions(request):
    return render(request, 'admissions.html')

def application(request):
    return render(request, "applecation.html", {})

def details(request):
    return render(request, "details.html", {})