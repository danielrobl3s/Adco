from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientesList.as_view(), name='clientes-list'),
]
