from rest_framework.response import Response
from rest_framework import status, generics
from .models import Prospectos
from .serializers import prospectoSerializer
from datetime import datetime


class Prospectos_c(generics.GenericAPIView):
    serializer_class = prospectoSerializer
    queryset = Prospectos.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        prospectos = Prospectos.objects.all()
        if search_param:
            prospectos = prospectos.filter(title__icontains=search_param)
        serializer = self.serializer_class(prospectos[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "prospectos": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "prospecto": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProspectoDetail(generics.GenericAPIView):
    queryset = Prospectos.objects.all()
    serializer_class = prospectoSerializer

    def get_note(self, pk):
        try:
            return Prospectos.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        prospecto = self.get_note(pk=pk)
        if prospecto == None:
            return Response({"status": "fail", "message": f"Prospecto with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(prospecto)
        return Response({"status": "success", "prospecto": serializer.data})

    def patch(self, request, pk):
        prospecto = self.get_note(pk)
        if prospecto == None:
            return Response({"status": "fail", "message": f"Prospecto with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            prospecto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "prospecto": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prospecto = self.get_note(pk)
        if prospecto == None:
            return Response({"status": "fail", "message": f"Prospecto with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        prospecto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)