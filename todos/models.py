from django.db import models

class Todo(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    finished_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM)  # Adicionando o campo priority
