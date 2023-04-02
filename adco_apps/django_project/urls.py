from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projectTrabajadores/', include('project_trabajadores_proveedores.urls')),
    path('api/trabajadoresP/', include('trabajadores_proveedores.urls')),
]