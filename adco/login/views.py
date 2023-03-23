from django.shortcuts import render
from .models import Usuario
from rest_framework import generics
from .serializers import UsuarioSerializer


class UsuarioCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new user
    queryset = Usuario.objects.all(),
    serializer_class = UsuarioSerializer


class UsuarioList(generics.ListAPIView):
    # API endpoint that allows user to be viewed.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer