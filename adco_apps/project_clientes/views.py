from rest_framework.response import Response
from rest_framework import status, generics
from .models import ProjectClientes
from .serializers import clienteSerializer
from datetime import datetime


class Project_clientesC(generics.GenericAPIView):
    serializer_class = clienteSerializer
    queryset = ProjectClientes.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        clientes = ProjectClientes.objects.all()
        if search_param:
            clientes = clientes.filter(title__icontains=search_param)
        serializer = self.serializer_class(clientes[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "clientes": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "cliente": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(generics.GenericAPIView):
    queryset = ProjectClientes.objects.all()
    serializer_class = clienteSerializer

    def get_note(self, pk):
        try:
            return ProjectClientes.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        cliente = self.get_note(pk=pk)
        if cliente == None:
            return Response({"status": "fail", "message": f"Cliente with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(cliente)
        return Response({"status": "success", "cliente": serializer.data})

    def patch(self, request, pk):
        cliente = self.get_note(pk)
        if cliente == None:
            return Response({"status": "fail", "message": f"Cliente with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "cliente": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cliente = self.get_note(pk)
        if cliente == None:
            return Response({"status": "fail", "message": f"Cliente with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)