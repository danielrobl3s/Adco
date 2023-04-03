from rest_framework.response import Response
from rest_framework import status, generics
from .models import ProjectGastos
from .serializers import project_gastoSerializer
from datetime import datetime


class Project_gastosC(generics.GenericAPIView):
    serializer_class = project_gastoSerializer
    queryset = ProjectGastos.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        gastos = ProjectGastos.objects.all()
        if search_param:
            gastos = gastos.filter(title__icontains=search_param)
        serializer = self.serializer_class(gastos[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "gastos": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "gasto": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class GastoDetail(generics.GenericAPIView):
    queryset = ProjectGastos.objects.all()
    serializer_class = project_gastoSerializer

    def get_note(self, pk):
        try:
            return ProjectGastos.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        gasto = self.get_note(pk=pk)
        if gasto == None:
            return Response({"status": "fail", "message": f"Gasto with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(gasto)
        return Response({"status": "success", "gasto": serializer.data})

    def patch(self, request, pk):
        gasto = self.get_note(pk)
        if gasto == None:
            return Response({"status": "fail", "message": f"Gasto with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            gasto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "gasto": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gasto = self.get_note(pk)
        if gasto == None:
            return Response({"status": "fail", "message": f"Gasto with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        gasto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)