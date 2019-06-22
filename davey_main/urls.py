from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='davey-home'),
    #pdf label views
    path('arborgreen_view/',views.arborgreen_view, name='arborgreen-pdf'),
    path('polyphosphite_view/',views.polyphosphite_view, name='polyphosphite-pdf'),
    path('adams_view/',views.adams_view, name="adams-pdf"),
    path('cambistat_view/',views.cambistat_view, name="cambistat-pdf"),
    path('florel_view/',views.florel_view, name='florel-pdf'),

    #other urls
    path('client_view/', views.client_view, name='client-view'),
    path('carrier/', views.carrier, name='carrier'),
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