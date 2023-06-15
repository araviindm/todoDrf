from rest_framework.decorators import api_view
from rest_framework.response import Response


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
