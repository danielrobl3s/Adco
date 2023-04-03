from django.urls import path
from .views import Project_gastosC, GastoDetail

urlpatterns = [
    path('', Project_gastosC.as_view()),
    path('<str:pk>', GastoDetail.as_view())
]