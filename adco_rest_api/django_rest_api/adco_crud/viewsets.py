from rest_framework import viewsets
from . import models
from . import serializers

class ProjectProveedoresTrabajadoresViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectProveedoresTrabajadores.objects.all()
    serializer_class = serializers.ProjectProveedoresTrabajadoresSerializer

    def list(self, request):
        return super().list(request)

    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    def create(self, request):
        return super().create(request)

    def update(self, request, pk=None):
        return super().update(request, pk)

    def destroy(self, request, pk=None):
        return super().destroy(request, pk)

