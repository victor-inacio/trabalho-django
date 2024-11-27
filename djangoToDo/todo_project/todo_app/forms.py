from django import forms
from django.contrib.auth.models import User
from .models import Task

# Formulário para Login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# Formulário para Gerenciar Tarefas
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline', 'done']
