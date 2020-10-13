from django.urls import path, include
from rest_framework import routers
from .views import HumanViewSet, UserViewSet, CreateHumanViewSet

router = routers.DefaultRouter()
router.register('humans', HumanViewSet)
router.register('createhumans', CreateHumanViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]