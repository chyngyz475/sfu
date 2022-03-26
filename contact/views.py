import json
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse, 
)
import email
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from . import models
from django.views.generic.edit import CreateView, FormView

from django.views.decorators.csrf  import csrf_exempt

from django.views.generic.edit import CreateView

from . import forms

from django.urls import reverse_lazy

class ContactCreateView(CreateView):
    model = models.Contact
    form_class = forms.ContactForm
    success_url = reverse_lazy("thanks")
    
def thanks(request):
    return render(request=request, template_name='thanks.html')
     
# def home(request: HttpRequest) -> HttpResponse:
    
#     if request.method=="POST":
#         print('test')
#         print(request.POST)
#         contact=Contact()
#         contact.name = request.POST.get('name')
#         contact.courses = request.POST.get('coursess')
#         contact.phone = request.POST.get('phone')
#         contact.email = request.POST.get('email')
#         contact.subject = request.POST.get('subject')
#         contact.save()
#         return HttpResponse("<h1>Спасибо заявка отправлено</h1>")
#     return render(request=request, template_name='contact/application.html')


# @csrf_exempt 
# def application(request: HttpRequest) -> JsonResponse:
#     if request.method=="POST":
#         print('test')
#         print(request.POST)
#         data = json.loads(request.body) 
#         contact=Contact()
#         contact.name = data['name']
#         contact.courses = data['courses']
#         contact.phone = data['phone']
#         contact.email = data['email']
#         contact.subject = data['subject']
#         contact.save()
#         return JsonResponse(data={'message':"<h1>Спасибо заявка отправлено</h1>"},status = 200)
    
     
#     return JsonResponse(data={'message':"Метод должен быть post"},status = 500)
 