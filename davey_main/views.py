from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.db import models
from .models import Employee
# Create your views here.

def home(request):
    if request.session.has_key('username'):
        username = request.session['username']
        office = 'STLWest 135831'
        return render(request, 'davey_main/home.html', {'username':office})
    else:    
        return render(request, 'davey_main/home.html')

def about(request):
    return render(request, 'davey_main/about.html')

def login(request):

    if request.method == 'GET':
        return render(request, 'davey_main/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        employee = Employee.objects.filter(username=username).first()

        username_error = 'Username not found'
        password_error = 'Password not valid. Please contact your administrator.'
        login_error = 'You are already logged in'

        if request.session.has_key('username'):
            return render(request, 'davey_main/login.html', {'login_error':login_error})

        else:

            if employee and employee.password == password:
    #           Django has a built in user authentication system. doing this like you would in flask may not be necessary. see auth url patterns in settings
                request.session['username'] = username
                
                return redirect(home)

            elif employee and employee.password != password:
                return render(request, 'davey_main/login.html', {'me':username, 'password_error':password_error})
        
            else:
                return render(request, 'davey_main/login.html', {'username_error':username_error, 'password_error':password_error})
        
def logout(request):
    try:
        del request.session['username']
    except:
        pass
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