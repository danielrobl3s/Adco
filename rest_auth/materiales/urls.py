from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaterialList.as_view(), name='materiales-list'),
    path('<pk>/', views.MaterialDetail.as_view(), name='materiales-detail'),
    path('recursos/', views.RecursoList.as_view(), name='recursos-list'),
    path('recursos/<pk>/', views.RecursoList.as_view(), name='recurso-details') #<------redirecciona a los prospectos donde esta la info de los clientes
]
