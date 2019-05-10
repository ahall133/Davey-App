from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='davey-home'),
    path('about/', views.about, name='davey-about'),
    path('logout/', views.logout, name='davey-logout'),
    path('login/', views.login, name= 'davey-login')
]