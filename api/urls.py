from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('todo/', views.todos, name="todos"),
    path('todo/<int:pk>/', views.todo, name="todo"),
]
