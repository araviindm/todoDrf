from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todos, name="todos"),
    path('todo/<int:pk>/', views.todo, name="todo"),
]
