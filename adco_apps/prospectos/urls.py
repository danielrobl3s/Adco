from django.urls import path
from .views import Prospectos_c, ProspectoDetail

urlpatterns = [
    path('', Prospectos_c.as_view()),
    path('<str:pk>', ProspectoDetail.as_view())
]