from django.urls import path
from .views import Project_clientesC, ClienteDetail

urlpatterns = [
    path('', Project_clientesC.as_view()),
    path('<str:pk>', ClienteDetail.as_view())
]