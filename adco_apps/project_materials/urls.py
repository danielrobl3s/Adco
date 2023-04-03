from django.urls import path
from .views import Project_materialsC, MaterialDetail

urlpatterns = [
    path('', Project_materialsC.as_view()),
    path('<str:pk>', MaterialDetail.as_view())
]