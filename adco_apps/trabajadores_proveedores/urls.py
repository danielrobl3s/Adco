from django.urls import path
from .views import Trabajadores_p, Trabajador_pDetail

urlpatterns = [
    path('', Trabajadores_p.as_view()),
    path('<str:pk>', Trabajador_pDetail.as_view())
]