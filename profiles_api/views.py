from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    # API View Test

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