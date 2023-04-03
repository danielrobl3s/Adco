from rest_framework.response import Response
from rest_framework import status, generics
from .models import ProjectMaterials
from .serializers import materialSerializer
from datetime import datetime


class Project_materialsC(generics.GenericAPIView):
    serializer_class = materialSerializer
    queryset = ProjectMaterials.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        materiales = ProjectMaterials.objects.all()
        if search_param:
            materiales = materiales.filter(title__icontains=search_param)
        serializer = self.serializer_class(materiales[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "materiales": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "material": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MaterialDetail(generics.GenericAPIView):
    queryset = ProjectMaterials.objects.all()
    serializer_class = materialSerializer

    def get_note(self, pk):
        try:
            return ProjectMaterials.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        material = self.get_note(pk=pk)
        if material == None:
            return Response({"status": "fail", "message": f"Material with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(material)
        return Response({"status": "success", "material": serializer.data})

    def patch(self, request, pk):
        material = self.get_note(pk)
        if material == None:
            return Response({"status": "fail", "message": f"Material with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            material, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "material": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        material = self.get_note(pk)
        if material == None:
            return Response({"status": "fail", "message": f"Material with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)