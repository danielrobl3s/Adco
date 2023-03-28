from django.urls import path
from . import views

urlpatterns = [
    path('', views.GastoList.as_view(), name='gastos-list'),
    #path('/<pk:int>', ClientesDetail.as_view(), name='detalles-cliente') #<------redirecciona a los prospectos donde esta la info de los clientes
]
