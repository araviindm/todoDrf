from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('todo/', views.todos, name="todos"),
    path('todo/<str:pk>/', views.todo, name="todo"),
]