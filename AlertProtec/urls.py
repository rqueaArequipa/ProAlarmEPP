from rest_framework import routers
from .api import MachineryViewSet, PersonViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('api/machinery', MachineryViewSet, 'machinery')
router.register('api/person', PersonViewSet, 'person')
router.register('api/user', UserViewSet, 'user')

urlpatterns = router.urls