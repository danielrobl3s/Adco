from django.urls import path
from . import views

urlpatterns = [
    path('', views.PgastoList.as_view(), name='gastos-list'),
    path('<pk>/', views.PgastoDetail.as_view(), name='detalles-cliente') #<------redirecciona a los prospectos donde esta la info de los clientes
]