from django.contrib import admin
from django.urls import path
from  .import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.courses, name='courses'),
    path('single/',  views.single, name='single'),
    path('contact/',  views.contact, name='contact'),
    path('admissions/',  views.admissions, name='admissions'),
    path('courses/',  views.courses, name='courses'),
    path('details/', views.details, name='details')
]