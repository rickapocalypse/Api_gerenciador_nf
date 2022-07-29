from django.urls import path
from . import views
urlpatterns = [
    path('notafiscal/', views.NotaFiscalList, name='notafiscal-list'),
]
