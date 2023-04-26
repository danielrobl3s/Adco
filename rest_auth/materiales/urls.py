from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaterialList.as_view(), name='materiales-list'),
    path('<pk>/', views.MaterialDetail.as_view(), name='materiales-detail'),
    path('filter/<str:proyecto>/', views.FmaterialList.as_view(), name='filter-materiales-list'),
    path('filter/<str:proyecto>/<pk>/', views.FmaterialDetail.as_view(), name='filter-materiales-detail'),
    path('recursos/', views.RecursoList.as_view(), name='recursos-list'),
    path('recursos/<pk>/', views.RecursoDetail.as_view(), name='recursos-details'), #<------redirecciona a los prospectos donde esta la info de los clientes
]
