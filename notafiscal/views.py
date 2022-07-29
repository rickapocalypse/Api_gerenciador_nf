from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def NotaFiscalList(request):
    return HttpResponse('NotaFiscalList')
    # return render(request, 'notafiscal/notafiscal_list.html')