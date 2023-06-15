from rest_framework import status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer


def get_todos():
    todos = Todo.objects.all().order_by('-time_stamp')
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


def get_todo(todo):
    serializer = TodoSerializer(todo)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_todo(request, pk):
    data = request.data
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def delete_todo(todo):
    todo.delete()
    return Response('Todo was deleted!')
