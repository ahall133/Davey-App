from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='davey-home'),
    path('about/', views.about, name='davey-about'),
    path('logout/', views.logout, name='davey-logout'),
    path('login/', views.login, name= 'davey-login'),
    path('tickets/', views.tickets, name= 'davey-tickets'),
    path('route/', views.route, name='davey-route'),
    path('phcmanual/', views.phcmanual, name='davey-phcmanual'),
    path('natureclock/', views.natureclock, name='davey-natureclock'),
    path('labels/', views.labels, name='davey-labels'),
    path('client_search/', views.client_search, name='davey-client_search'),
    path('calculator/', views.calculator, name='davey-calculator')
]