from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientesList.as_view(), name='clientes-list'),
    path('<pk>/', views.ClientesDetail.as_view(), name='detalles-cliente') #<------redirecciona a los prospectos donde esta la info de los clientes
]
