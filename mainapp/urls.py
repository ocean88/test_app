from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FactoryViewSet,
    RetailNetworkViewSet,
    EntrepreneurViewSet,
    ProductViewSet,
)

router = DefaultRouter()
router.register(r'factories', FactoryViewSet, basename='factory')
router.register(r'retail-networks', RetailNetworkViewSet, basename='retail-network')
router.register(r'entrepreneurs', EntrepreneurViewSet, basename='entrepreneur')
router.register(r'products', ProductViewSet, basename='product')

app_name = 'mainapp'

urlpatterns = [
    path('', include(router.urls)),
]