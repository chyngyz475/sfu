
from hashlib import new
from django.views.generic import ListView
import pdb
from django.shortcuts import render


def home(request):
    return render(
        request, 'base.html'
        )

def courses(request):
    return render(
        request, 'courses.html'
        )

def bachelor(request):
    return render(
        request, 'bachelor.html'
        )

def contact1(request):
    return render(
        request, 'contact1.html'
        )

def single(request):
    return render(
        request, 'single.html'
        )

def blog(request):
    return render(
        request, 'blog.html'
        )

def blog(request):
    return render(
        request, 'blog.html'
        )

def admissions(request):
    
    return render(
        request, 'admissions.html'
        )

def application(request):
    return render(
        request, "aplication.html",
        )

def details(request):
    return render(
        request, "details.html",
        )

def university_admission(request):
    return render(
        request, "university_admission.html",
        )

def details_post(request):
    return render(request=request, template_name='item/details_post.html')

def details_post2(request):
    return render(request=request, template_name='item/details_post2.html')

def details_post3(request):
    return render(request=request, template_name='item/details_post.html')



def news (request):
    return render(request=request, template_name='news.html')