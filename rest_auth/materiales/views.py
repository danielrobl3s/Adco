from rest_framework import generics, permissions
from .models import Materiales, Recursos
from .serializers import MaterialSerializer, RecursoSerializer

class MaterialList(generics.ListCreateAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Materiales.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class RecursoList(generics.ListCreateAPIView):
    serializer_class = RecursoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recursos.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

