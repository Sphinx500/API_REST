from email.mime import message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer

class HelloApiView(APIView):
    # API View Test
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        # Return APIView list
        an_apiview = {
            'Using HTTP Methods as functions (get,post,patch,put,delete)',
            'Its like a normal Django View',
            'Provides a better logic control of application',
            'Its mapping manually the URL parameters',
        }
        # Define an APIVIEW
        return Response({'message':'Hello', 'an_apiview':an_apiview})
    
    def post(self, request):
        # Create a Message with our name
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} '
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )