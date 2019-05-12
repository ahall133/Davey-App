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

def tickets(request):
    return render(request, 'davey_main/tickets.html')

def client_search(request):
    return render(request, 'davey_main/client_search.html')

def route(request):
    return render(request, 'davey_main/route.html')

def calculator(request):
    return render(request, 'davey_main/calculator.html')

def labels(request):
    return render(request, 'davey_main/labels.html')

def phcmanual(request):
    return render(request, 'davey_main/phcmanual.html')
    
def natureclock(request):
    return render(request, 'davey_main/natureclock.html')