from django.urls import path
from todos import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('registerp/', views.product_register, name='product_register'),
    path('edit/<int:pk>/', views.product_edit, name='product_edit'),  # Editar uma tarefa com ID
    path('list/', views.product_list, name='product_list'),  # Lista todas as tarefas
    path('product/delete/', views.product_delete, name='product_delete'),
]
