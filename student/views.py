import pdb
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
)
from django.views import View

 
def index(request):
    
    return TemplateResponse(request, "templates/index.html")