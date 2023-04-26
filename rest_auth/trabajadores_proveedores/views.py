from rest_framework import generics, permissions
from .models import TrabajadoresProveedores
from .serializers import TrabajadoresProveedoresSerializer

class TrabajadoresProveedoresList(generics.ListCreateAPIView):
    serializer_class = TrabajadoresProveedoresSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TrabajadoresProveedores.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TrabajadoresProveedoresDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrabajadoresProveedoresSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TrabajadoresProveedores.objects.filter(created_by=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)