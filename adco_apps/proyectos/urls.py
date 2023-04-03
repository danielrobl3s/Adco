from django.urls import path
from .views import Proyectos_c, ProyectoDetail

urlpatterns = [
    path('', Proyectos_c.as_view()),
    path('<str:pk>', ProyectoDetail.as_view())
]