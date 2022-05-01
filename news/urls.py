from django.contrib import admin
from django.urls import path
from  .import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('single/',  views.single, name='single'),
    path('contact/',  views.contact1, name='contact1'),
    path('admissions/',  views.admissions, name='admissions'),
    path('courses/',  views.courses, name='courses'),
    path('details/', views.details, name='details'),
    path('university_admission/', views.university_admission, name='university_admission'),
    path('bachelor/', views.bachelor, name='bachelor'),
    path("details_post", views.details_post, name="details_post"),
    path("details_post2", views.details_post2, name="details_post2"),
    path("details_post3", views.details_post3, name="details_post3")
    
]
