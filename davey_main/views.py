from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Employee
# Create your views here.

def home(request):
    return render(request, 'davey_main/home.html')

def about(request):
    return render(request, 'davey_main/about.html')

#TODO ---login form functionality working need to add error statements---
def login(request):

    if request.method == 'GET':
        return render(request, 'davey_main/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        employee = Employee.objects.filter(username=username).first()

#        print(username)
#        print(password)
#        print(employee)
#        print(employee.username)

        if employee and employee.password == password:
            return HttpResponse('even better')

        return HttpResponse('ok')
       

        
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