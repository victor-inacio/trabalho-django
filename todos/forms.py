from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'deadline', 'finished_at']  # Adicione os campos necessários
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'finished_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
