from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
        Test API endpoint
    """

    def get(self, request, format=None):
        """
            Returns a list of APIView features
        """
        an_apiview = [
            'use http methods',
            'Is similar to trditional ',
            'givrs you most',
            'is mapped manually to url'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
