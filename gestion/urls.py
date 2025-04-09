from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('client/add/', views.client_create, name='client_add'),
    path('assurances/', views.assurance_list, name='assurance_list'),
    path('assurance/add/', views.assurance_create, name='assurance_add'),
]