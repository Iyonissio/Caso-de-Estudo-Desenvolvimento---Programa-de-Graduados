import json
from django.shortcuts import render
from .models import Employeer, Formation, Notario, PaymentsControlUssd, PaymentsControlUssdMercados, RequestControlUssd, Transporte, Quiz, RequestsUssd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.models import AuthToken
from django.contrib.auth import authenticate
from rest_framework import serializers, views, viewsets, permissions, generics
from .serializers import AddFormationSerializer, NotarioSerializer, QuizSerializer, EmployeerSerializer, FormationSerializer, PaymentsControlSerialazer, PaymentsControlMercadosSerialazer, RegisterSerializer, RequestControlUssdSerializer, TransporteSerializer, UserSerializer, RequestsUssdSerializer
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
# Annotate
from django.db.models import Count
from rest_framework.views import APIView
from django.core.serializers.json import DjangoJSONEncoder

# Other
# Dds



class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Requisicoes ussd


class UssdRequestControl(viewsets.ModelViewSet):
    queryset = RequestControlUssd.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_serializer_class(self):
        return RequestControlUssdSerializer

    def add(self, request):
        queryset = RequestControlUssd.objects.all()
        serializer = RequestControlUssdSerializer(queryset, many=True)
        return Response(serializer.data)


class UssdRequests(viewsets.ModelViewSet):
    queryset = RequestsUssd.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_serializer_class(self):
        return RequestsUssdSerializer

    def add(self, request):
        queryset = RequestsUssd.objects.all()
        serializer = RequestsUssdSerializer(queryset, many=True)
        return Response(serializer.data)


class UssdRequestsOperadoras(viewsets.ModelViewSet):
    queryset = RequestsUssd.objects.filter()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_serializer_class(self):
        return RequestsUssdSerializer

    # def add(self, request):
    #     queryset = RequestsUssd.objects.filter.all()
    #     serializer = RequestsUssdSerializer(queryset, many=True)
    #     return Response(serializer.data)


class UssdPaymentsControl(viewsets.ModelViewSet):
    queryset = PaymentsControlUssd.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_serializer_class(self):
        return PaymentsControlSerialazer

    def add(self, request):
        queryset = PaymentsControlUssd.objects.all()
        serializer = PaymentsControlSerialazer(queryset, many=True)
        return Response(serializer.data)

