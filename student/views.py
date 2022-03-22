
import pdb
from django.shortcuts import redirect, render
from django.views import View
from .models import * 


class AplicationView(View):
    def post(self,request):
        form = AplicationView(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")

def home(request):
    return render(request, 'base.html')
