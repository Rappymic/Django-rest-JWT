from curses import ACS_PLUS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    '''is required for authentication check'''
    def get(self, request):
        pass
