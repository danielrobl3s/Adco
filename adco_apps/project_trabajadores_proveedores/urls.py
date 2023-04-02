from django.urls import path
from .views import Proveedores, ProveedorDetail

urlpatterns = [
    path('', Proveedores.as_view()),
    path('<str:pk>', ProveedorDetail.as_view())
]
