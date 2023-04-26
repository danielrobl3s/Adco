from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProspectosList.as_view(), name='prospectos-detail'),
    path('<pk>/', views.ProspectosDetail.as_view(), name='proyectos-detail')
]