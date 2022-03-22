from ast import pattern
from django.conf.urls import *
from django.conf import settings
from  views import *

urlpatterns = pattern('',
    # Example:
    (r'contact/$',contact),
    (r'^thanks/$', thanks),

)