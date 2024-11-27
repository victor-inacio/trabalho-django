from django.db import models
from django.contrib.auth.models import User

# Modelo de Tarefa
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona a tarefa com o usuário
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    priority = models.IntegerField(default=1)  # 1=Baixa, 2=Média, 3=Alta
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)  # Status da tarefa
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)  # Subtarefa

    def __str__(self):
        return self.title
