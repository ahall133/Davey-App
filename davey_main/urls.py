from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='davey-home'),
    path('about/', views.about, name='davey-about')
]