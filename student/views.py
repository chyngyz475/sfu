
import pdb
from django.shortcuts import render
from django.http import HttpResponse
from news.models import Post
from .models import * 


def home(request):
    return render(request, 'base.html')
