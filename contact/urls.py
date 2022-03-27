from django.urls import path 
from . import views 
from django.contrib import admin


urlpatterns = [
    # path('application', views.application,name='application'),
    path("app", views.ContactCreateView.as_view(), name="application"),
    path("thanks", views.thanks, name="thanks"),
]

