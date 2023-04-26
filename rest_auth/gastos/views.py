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
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class GastoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GastoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Gastos.objects.filter(created_by=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#Filter based on the ID

class FgastoList(generics.ListCreateAPIView):
    serializer_class = GastoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        proyecto = self.kwargs.get('proyecto')
        return Gastos.objects.filter(created_by=self.request.user, proyecto=proyecto)

    def perform_create(self, serializer):
        proyecto = self.kwargs.get('proyecto')
        serializer.save(created_by=self.request.user, proyecto=proyecto)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class FgastoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GastoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        proyecto = self.kwargs.get('proyecto')
        return Gastos.objects.filter(created_by=self.request.user, proyecto=proyecto)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)