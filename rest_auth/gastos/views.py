from rest_framework import generics, permissions
from .models import Gastos
from .serializers import GastoSerializer

class GastoList(generics.ListCreateAPIView):
    serializer_class = GastoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Gastos.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class GastoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GastoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Gastos.objects.filter(created_by=self.request.user)

