
from django.contrib import admin
from django.urls import path

from todos.views import login, register, product_register, product_edit,product_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('register/', register),
    path('registerp/', product_register),
    path('edit/', product_edit),
    path('list/', product_list),
]
