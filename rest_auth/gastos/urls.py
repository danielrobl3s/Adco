from django.urls import path
from . import views

urlpatterns = [
    path('', views.GastoList.as_view(), name='gastos-list'),
    path('<pk>/', views.GastoDetail.as_view(), name='gastos-detail'), #<------redirecciona a los prospectos donde esta la info de los clientes
    path('filter/<str:proyecto>/', views.FgastoList.as_view(), name='filter-gastos-list'),
    path('filter/<str:proyecto>/<pk>/', views.FgastoDetail.as_view(), name='filter-gastos-detail'),

]
