from django.urls import path, include
from rest_framework import routers
from .views import PortViewSet

router = routers.DefaultRouter()
router.register(r'ports', PortViewSet)

urlpatterns = [
    path('api/ports/', include(router.urls))
]
