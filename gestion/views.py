from django.shortcuts import render, redirect
from .models import Client, Assurance
from .forms import ClientForm, AssuranceForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'gestion/client_list.html', {'clients': clients})

def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'gestion/client_form.html', {'form': form})

def assurance_list(request):
    assurances = Assurance.objects.select_related('client').all()
    return render(request, 'gestion/assurance_list.html', {'assurances': assurances})

def assurance_create(request):
    form = AssuranceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('assurance_list')
    return render(request, 'gestion/assurance_form.html', {'form': form})