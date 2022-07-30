from django.urls import path
from . import views

urlpatterns = [
    path('', views.providers, name='providers-view'),
]