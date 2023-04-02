from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/proveedores/', include('project_trabajadores_proveedores.urls')),
]