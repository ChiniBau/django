from django import forms
from .models import Task    
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
        
class RegistrationForm(UserCreationForm):
    email=forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):    
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']
        
