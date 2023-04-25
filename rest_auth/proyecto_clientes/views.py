from rest_framework import generics, permissions
from .models import Clientes
from .serializers import ClientesSerializer


class PclientesList(generics.ListCreateAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Clientes.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PclientesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Clientes.objects.filter(created_by=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)