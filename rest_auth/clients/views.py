from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, permissions
from .models import Clientes
from .serializers import ClientesSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from django.http import JsonResponse


class ClientesList(generics.ListCreateAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Clientes.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Clientes.objects.filter(created_by=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@csrf_exempt
def get_tokens(request):
    token, created = Token.objects.get_or_create(user=request.user)
    return JsonResponse({'csrf_token': request.COOKIES.get('csrftoken'), 'auth_token': token.key})
