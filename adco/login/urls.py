from django.urls import include, path
from .views import UsuarioCreate, UsuarioList, UsuarioDetail, UsuarioUpdate, UsuarioDelete


urlpatterns = [
    path('create/', UsuarioCreate.as_view(), name='create-usuario'),
    path('', UsuarioList.as_view()),
    path('<int:pk>/', UsuarioDetail.as_view(), name='retrieve-usuario'),
    path('update/<int:pk>/', UsuarioUpdate.as_view(), name='update-usuario'),
    path('delete/<int:pk>/', UsuarioDelete.as_view(), name='delete-usuario')
]