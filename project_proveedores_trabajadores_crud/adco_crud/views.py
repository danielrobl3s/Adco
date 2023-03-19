from rest_framework.response import Response
from rest_framework import status, generics
from .models import ProjectProveedoresTrabajadores
from .serializers import proveedorSerializer
from datetime import datetime


class Proveedores(generics.GenericAPIView):
    serializer_class = proveedorSerializer
    queryset = ProjectProveedoresTrabajadores.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        proveedores = ProjectProveedoresTrabajadores.objects.all()
        if search_param:
            proveedores = proveedores.filter(title__icontains=search_param)
        serializer = self.serializer_class(proveedores[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "proveedores": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "proveedor": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProveedorDetail(generics.GenericAPIView):
    queryset = ProjectProveedoresTrabajadores.objects.all()
    serializer_class = proveedorSerializer

    def get_note(self, pk):
        try:
            return ProjectProveedoresTrabajadores.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        proveedor = self.get_note(pk=pk)
        if proveedor == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(proveedor)
        return Response({"status": "success", "proveedor": serializer.data})

    def patch(self, request, pk):
        proveedor = self.get_note(pk)
        if proveedor == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            proveedor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "proveedor": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        proveedor = self.get_note(pk)
        if proveedor == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
