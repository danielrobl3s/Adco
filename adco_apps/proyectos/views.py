from rest_framework.response import Response
from rest_framework import status, generics
from .models import Proyectos
from .serializers import proyectoSerializer
from datetime import datetime


class Proyectos_c(generics.GenericAPIView):
    serializer_class = proyectoSerializer
    queryset = Proyectos.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        proyectos = Proyectos.objects.all()
        if search_param:
            proyectos = proyectos.filter(title__icontains=search_param)
        serializer = self.serializer_class(proyectos[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "proyectos": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "proyecto": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProyectoDetail(generics.GenericAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = proyectoSerializer

    def get_note(self, pk):
        try:
            return Proyectos.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        proyecto = self.get_note(pk=pk)
        if proyecto == None:
            return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(proyecto)
        return Response({"status": "success", "project": serializer.data})

    def patch(self, request, pk):
        proyecto = self.get_note(pk)
        if proyecto == None:
            return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            proyecto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "project": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        proyecto = self.get_note(pk)
        if proyecto == None:
            return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        proyecto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)