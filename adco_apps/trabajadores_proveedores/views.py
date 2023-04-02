from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, generics
from .models import TrabajadoresProveedores
from .serializers import trabajadores_pSerializer
from datetime import datetime


class Trabajadores_p(generics.GenericAPIView):
    serializer_class = trabajadores_pSerializer
    queryset = TrabajadoresProveedores.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        trabajadores_p = TrabajadoresProveedores.objects.all()
        if search_param:
            trabajadores_p = trabajadores_p.filter(title__icontains=search_param)
        serializer = self.serializer_class(trabajadores_p[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "trabajadores_p": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "trabajador_p": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Trabajador_pDetail(generics.GenericAPIView):
    queryset = TrabajadoresProveedores.objects.all()
    serializer_class = trabajadores_pSerializer

    def get_note(self, pk):
        try:
            return TrabajadoresProveedores.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        trabajador_p = self.get_note(pk=pk)
        if trabajador_p == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(trabajador_p)
        return Response({"status": "success", "trabajador_p": serializer.data})

    def patch(self, request, pk):
        trabajador_p = self.get_note(pk)
        if trabajador_p == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            trabajador_p, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "trabajador_p": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        trabajador_p = self.get_note(pk)
        if trabajador_p == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        trabajador_p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
