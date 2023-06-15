from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import Todo
from .utils import get_todos, get_todo, create_todo, update_todo, delete_todo


# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/todo/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of todos'
        },
        {
            'Endpoint': '/todo/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single todo object'
        },
        {
            'Endpoint': '/todo/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new todo with data sent in post request'
        },
        {
            'Endpoint': '/todo/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing note with data sent in put request'
        },
        {
            'Endpoint': '/todo/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting todo'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def todos(request):
    if request.method == 'GET':
        return get_todos()

    elif request.method == 'POST':
        return create_todo(request)


@api_view(['GET', 'PUT', 'DELETE'])
def todo(request, pk):
    try:
        todo_obj = Todo.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get_todo(todo_obj)

    elif request.method == 'PUT':
        return update_todo(todo_obj, request)

    elif request.method == 'DELETE':
        return delete_todo(todo_obj)
