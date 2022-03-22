from django.contrib import admin
from django.urls import path,include
from  .import views
from .views import AplicationView
 
urlpatterns = [
    path('<page_slug>-<page_id>/', include([
        path('', views.home),
        path('', AplicationView.as_view(), name='aplication_view')
    ])),
]