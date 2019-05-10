from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'davey_main/home.html')

def about(request):
    return render(request, 'davey_main/about.html')

def login(request):
    return render(request, 'davey_main/login.html')

def logout(request):
    return render(request, 'davey_main/logout.html')