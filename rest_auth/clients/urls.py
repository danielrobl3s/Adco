from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientesList.as_view(), name='clientes-list'),
    path('<pk>/', views.ClientesDetail.as_view(), name='detalles-cliente'), #<------redirecciona a los prospectos donde esta la info de los clientes
    path('filter/<str:proyecto>/', views.FclientesList.as_view(), name='Filter-clientes-list'),
    path('filter/<str:proyecto>/<pk>/', views.FclientesDetail.as_view(), name="Filter-detalles-cliente"),
]
