from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import *

def contact(request):

    form = ReCaptchaForm()
    if request.POST:
        form = ReCaptchaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['my@mail.ru'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ReCaptchaForm()
    return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))


def thanks(request):
    return render_to_response('thanks.html')