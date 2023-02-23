from adco_crud.viewsets import ProjectProveedoresTrabajadoresViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ProjectProveedoresTrabajadores', ProjectProveedoresTrabajadoresViewSet)