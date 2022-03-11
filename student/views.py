import pdb
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
)
from django.views import View

 
def index(request):
    
    return render(request, "templates/index.html")