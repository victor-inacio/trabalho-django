from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

# Função para mostrar a tela de login
def login(request):
    return render(request, "todos/login.html")

# Função para mostrar a tela de registro
def register(request):
    return render(request, "todos/register.html")

# Função para mostrar o formulário de registro de produto
def product_register(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        deadline = request.POST['deadline']

        # Criação de um novo objeto Todo
        todo = Todo(
            title=title,
            description=description,
            priority=priority,
            deadline=deadline
        )
        todo.save()
        return redirect('product_list')  # Redireciona para a lista de produtos/tarefas

    return render(request, "todos/product-register.html")

# Função para editar um produto
def product_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redireciona para a lista de tarefas após salvar
    else:
        form = TodoForm(instance=todo)
    return render(request, "todos/product-edit.html", {"form": form})

# Função para listar todas as tarefas
def product_list(request):
    todos = Todo.objects.all().order_by('priority')  # Ordena pela prioridade
    return render(request, 'todos/product-list.html', {'todos': todos})

# Função para excluir uma tarefa
def product_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('product_list')  # Redireciona para a lista de tarefas após deletar
