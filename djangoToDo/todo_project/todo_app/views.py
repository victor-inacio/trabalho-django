from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import LoginForm, TaskForm

# Tela de Login com autenticação direta
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Autenticação do usuário
            user = authenticate(request, username=username, password=password)
            if user:  # Usuário autenticado
                login(request, user)  # Cria a sessão
                return redirect('home_page')
            else:  # Usuário não encontrado ou senha inválida
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Usuário ou senha inválidos.'
                })
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout do usuário
def logout_view(request):
    logout(request)
    return redirect('login')

# Página inicial (apenas para usuários logados)
@login_required
def home_page(request):
    tasks = Task.objects.filter(user=request.user)  # Mostra tarefas do usuário logado
    return render(request, 'home_page.html', {'tasks': tasks})

# Criar uma nova tarefa
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Relaciona a tarefa ao usuário logado
            task.save()
            return redirect('home_page')
    else:
        form = TaskForm()
    return render(request, 'task_register.html', {'form': form})

# Editar tarefa existente
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


# Defina as credenciais para autenticação básica
AUTHORIZED_EMAIL = "admin@example.com"
AUTHORIZED_PASSWORD = "password123"

def authenticate_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verifica se o email e a senha correspondem às credenciais autorizadas
        if email == AUTHORIZED_EMAIL and password == AUTHORIZED_PASSWORD:
            return render(request, 'login.html', {'success': True})
        else:
            return render(request, 'login.html', {'error': True, 'email': email})

    # Renderiza o formulário vazio caso o método não seja POST
    return render(request, 'login.html')