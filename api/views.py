from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .utils import get_todos, get_todo, create_todo, update_todo, delete_todo


@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def todos(request):
    if request.method == 'GET':
        return get_todos()

    elif request.method == 'POST':
        return create_todo(request)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def todo(request, pk):
    try:
        todo_obj = Todo.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(data="Not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get_todo(todo_obj)

    elif request.method == 'PUT':
        return update_todo(request, todo_obj)

    elif request.method == 'DELETE':
        return delete_todo(todo_obj)
