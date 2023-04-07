from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProyectoList.as_view(), name='proyectos-list'),
    path('<pk>/', views.ProyectoDetail.as_view(), name='proyectos-detail')
]