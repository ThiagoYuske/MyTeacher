from rest_framework.views import APIView
from rest_framework.response import Response

class HomeAPIView(APIView):

    def get(self, request, format=None):

        return Response({"nome": "Thiago", "idade": 24}, status=200)