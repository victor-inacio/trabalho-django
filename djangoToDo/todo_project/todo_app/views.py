from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import LoginForm, TaskForm

# Tela de Login
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home_page')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Usuário ou senha inválidos'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Página inicial
@login_required
def home_page(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home_page.html', {'tasks': tasks})

# Criar tarefa
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home_page')
    else:
        form = TaskForm()
    return render(request, 'task_register.html', {'form': form})

# Editar tarefa
@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_register.html', {'form': form})

# Excluir tarefa
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('home_page')
