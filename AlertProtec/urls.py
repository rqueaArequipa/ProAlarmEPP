from rest_framework.routers import DefaultRouter
from .views import MachineryViewSet, PersonViewSet, UserViewSet, AlertViewSet
from django.urls import path, include

router = DefaultRouter()

router.register('machinery', MachineryViewSet, 'machinery')
router.register('person', PersonViewSet, 'person')
router.register('user', UserViewSet, 'user')
router.register('Alert', AlertViewSet, 'alert')
urlpatterns = [
    path('',include(router.urls))
]