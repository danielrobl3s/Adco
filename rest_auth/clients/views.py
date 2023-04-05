from django.views.decorators.csrf import ensure_csrf_cookie
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

    @ensure_csrf_cookie
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Clientes.objects.filter(created_by=self.request.user)

    @ensure_csrf_cookie
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @ensure_csrf_cookie
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @ensure_csrf_cookie
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
