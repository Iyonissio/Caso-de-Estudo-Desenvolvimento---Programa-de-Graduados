import re
#from telnetlib import STATUS
#from tkinter.messagebox import YES
from rest_framework import serializers, authentication, permissions
from rest_framework.serializers import Serializer
from api.models import Employeer
from rest_framework import viewsets, permissions
from .serializers import  EmployeerSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status


class EmployeerViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.headers)
        employ = Employeer.objects.all()
        serializer = EmployeerSerializer(employ, many=True)
        return Response(serializer.data)



