from django.shortcuts import render
import json  
import requests
from .data import thisdict
from forex_python.converter import CurrencyRates
from django.contrib import messages
# Create your views here.

    
def index(request):
       if request.method=='POST':
         cr = CurrencyRates()
         data1=str(request.POST.get('key1').upper())
         data2=str(request.POST.get('key2').upper())
         data3=int(request.POST.get('am'))
         from currency_converter import CurrencyConverter
         c = CurrencyConverter()
         a=c.convert(data3, data1, data2)
         messages.success(request,a)
         return render(request,'index.html',{'thisdict':thisdict,'data':a})
       else:
           return render(request,'index.html',{'thisdict':thisdict})