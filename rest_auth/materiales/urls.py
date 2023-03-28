from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaterialList.as_view(), name='materiales-list'),
    path('recursos/', views.RecursoList.as_view(), name='recursos-list'),
    #path('/<pk:int>', ClientesDetail.as_view(), name='detalles-cliente') #<------redirecciona a los prospectos donde esta la info de los clientes
]
