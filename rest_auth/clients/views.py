from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, permissions
from .models import Clientes
from .serializers import ClientesSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import login
from dj_rest_auth.views import LoginView
from proyectos.models import Proyecto


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
    
    #Filter by project id only
    
class FclientesList(generics.ListCreateAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        proyecto = self.kwargs.get('proyecto')
        return Clientes.objects.filter(created_by=self.request.user, proyecto=proyecto)

    def perform_create(self, serializer):
        proyecto = self.kwargs.get('proyecto')
        serializer.save(created_by=self.request.user, proyecto=proyecto)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class FclientesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        proyecto = self.kwargs.get('proyecto')
        return Clientes.objects.filter(created_by=self.request.user, proyecto=proyecto)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            token = Token.objects.get(user=self.user)
            response_data = response.data
            response_data['token'] = token.key
            response_data['sessionid'] = self.request.session.session_key
            response_data['csrftoken'] = get_token(request)
            response.data = response_data
            response.set_cookie(key='sessionid', value=self.request.session.session_key, httponly=True)
        return response


@csrf_exempt
def get_tokens(request):
    token, created = Token.objects.get_or_create(user=request.user)
    return JsonResponse({'csrf_token': request.COOKIES.get('csrftoken'), 'auth_token': token.key})
