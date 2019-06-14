from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
#from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,FileResponse,Http404
from django.db import models
from .models import Employee, Ticket

# Create your views here.

def home(request):
    if request.session.has_key('username'):
        username = request.session['username']
        office = 'STLWest 135831'
        return render(request, 'davey_main/home.html', {'username':office})
    else:    
        return render(request, 'davey_main/home.html')

# PDF VIEWS         
def arborgreen_view(request):
    try:
        return FileResponse(open('davey_main/static/davey_main/images/arborgreen.pdf', 'rb'), content_type='arborgreen.pdf')
    except FileNotFoundError:
        raise Http404()

def polyphosphite_view(request):
    try:
        return FileResponse(open('davey_main/static/davey_main/images/polyphosphite.pdf', 'rb'), content_type= 'polyphosphite.pdf')
    except FileNotFoundError:
        raise Http404()    

def adams_view(request):
    try:
        return FileResponse(open('davey_main/static/davey_main/images/adams.pdf', 'rb'), content_type= 'adams.pdf')
    except FileNotFoundError:
        raise Http404()    

def florel_view(request):
    try:
        return FileResponse(open('davey_main/static/davey_main/images/florel.pdf', 'rb'), content_type= 'florel.pdf')
    except FileNotFoundError:
        raise Http404()    

def cambistat_view(request):
    try:
        return FileResponse(open('davey_main/static/davey_main/images/Cambistat_SDS.pdf', 'rb'), content_type= 'cambistat.pdf')
    except FileNotFoundError:
        raise Http404()  

# END PDF VIEWS
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
    showing = 'Showing all open tickets...'
    tickets = Ticket.objects.all()

    if request.method == 'GET':
        return render(request, 'davey_main/tickets.html', {'tickets':tickets, 'showing':showing})
    if request.method == 'POST':

#        !!trying to figure out how to query multiple things at once and pass to template!!
        service = [request.POST.get('AG Pro'), request.POST.get('Inspect and Treat'), request.POST.get('EAB')]
        services = ['AG PRO', 'I&T', 'EAB']

        season = request.POST.get('Spring'), request.POST.get('Summer'), request.POST.get('Fall'), request.POST.get('Winter')
        seasons = ['Spring','Summer','Fall','Winter']

        
        tickets = Ticket.objects.all()
        service_holder = []
        season_holder = []
        service_filters = False
        season_filters = False
        
        
        
        idx = -1
        for i in service:
            idx += 1
            if i == 'on':
                service_filters = True
                service_holder.append(services[idx])
                

        idx = -1
        for i in season:
            idx += 1
            if i == 'on':
                season_filters = True
                season_holder.append(seasons[idx])

        if service_filters and not season_filters:
            tickets = Ticket.objects.filter(ticket_type__in=service_holder)
        elif season_filters and not service_filters:
            tickets = Ticket.objects.filter(ticket_season__in=season_holder)
        elif service_filters and season_filters:
            tickets = Ticket.objects.filter(ticket_type__in=service_holder).filter(ticket_season__in=season_holder)
        else:
            tickets = Ticket.objects.all()

        return render(request, 'davey_main/tickets.html', {'tickets':tickets, 'showing':showing})
        

def client_search(request):
    return render(request, 'davey_main/client_search.html')

def route(request):
    return render(request, 'davey_main/route.html')

def calculator(request):
    return render(request, 'davey_main/calculator.html')

def labels(request):
    return render(request, 'davey_main/labels.html')
    # Create the HttpResponse object with the appropriate PDF headers.
    #response = HttpResponse(content_type='davey_main/images/Cambistat_SDS.pdf')
    #response['Content-Disposition'] = 'attachment;filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    #p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    #p.showPage()
    #p.save()
    return response 


def phcmanual(request):
    return render(request, 'davey_main/phcmanual.html')
    
def natureclock(request):
    return render(request, 'davey_main/natureclock.html')