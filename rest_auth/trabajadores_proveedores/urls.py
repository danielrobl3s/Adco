from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrabajadoresProveedoresList.as_view(), name='trabajadores_proveedoresList'),
    path('<pk>/', views.TrabajadoresProveedoresDetail.as_view(), name='trabajadores_proveedores_detail')
]