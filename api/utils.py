from rest_framework import status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer


def get_todos():
    todos = Todo.objects.all().order_by('-time_stamp')
    serializer = TodoSerializer(todos, many=True)
    processed_todos = []
    for todo in serializer.data:
        if todo["tags"] is not None:
            tags = process_todo(todo["tags"])
            todo["tags"] = tags
            processed_todos.append(todo)
        else:
            todo["tags"] = None
            processed_todos.append(todo)

    return Response(processed_todos)


def process_todo(tags):
    tag_list = []
    start_index = None
    for i, item in enumerate(tags):
        if item == "'":
            if start_index is None:
                start_index = i + 1
            else:
                string = ''.join(tags[start_index:i])
                tag_list.append(string)
                start_index = None

    return tag_list


def get_todo(todo):
    serializer = TodoSerializer(todo)
    todo_obj = serializer.data
    tags = serializer.data["tags"]
    processed_tags = process_todo(tags)
    todo_obj["tags"] = processed_tags
    return Response(todo_obj)


def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_todo(request, todo):
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_todo(todo):
    todo.delete()
    return Response(data="Todo deleted", status=status.HTTP_204_NO_CONTENT)
