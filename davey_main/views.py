from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'davey_main/home.html')

def about(request):
    return HttpResponse('<h1>Davey About</h1>')