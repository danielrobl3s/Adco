from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Prospectos
from .serializers import ProspectosSerializer 

class ProspectosList(generics.ListCreateAPIView):
    serializer_class = ProspectosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Prospectos.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProspectosDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProspectosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Prospectos.objects.filter(created_by=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)