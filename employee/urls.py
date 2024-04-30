from django.contrib import admin
from django.urls import path,include
from adminsite import views
from employee import urls

urlpatterns = [
    path('',views.customershow),
]