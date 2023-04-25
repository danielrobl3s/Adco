from django.urls import path
from . import views

urlpatterns = [
    path('', views.PmaterialList.as_view(), name='proyecto-materiales-list'),
    path('<pk>/', views.PmaterialDetail.as_view(), name='proyecto-materiales-detail'),
]