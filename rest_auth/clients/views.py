from rest_framework import generics, permissions
from .models import Clientes
from .serializers import ClientesSerializer

class ClientesList(generics.ListCreateAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Clientes.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Clientes.objects.filter(created_by=self.request.user)

