from django import forms
from .models import Client, Assurance

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class AssuranceForm(forms.ModelForm):
    class Meta:
        model = Assurance
        fields = '__all__'