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
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Materiales.objects.filter(created_by=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    #Filter based on the ID
    
class FmaterialList(generics.ListCreateAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        proyecto = self.kwargs.get('proyecto')
        return Materiales.objects.filter(created_by=self.request.user, proyecto=proyecto)

    def perform_create(self, serializer):
        proyecto = self.kwargs.get('proyecto')
        serializer.save(created_by=self.request.user, proyecto=proyecto)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class FmaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        proyecto = self.kwargs.get('proyecto')
        return Materiales.objects.filter(created_by=self.request.user, proyecto=proyecto)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
class RecursoList(generics.ListCreateAPIView):
    serializer_class = RecursoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recursos.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RecursoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecursoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recursos.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
