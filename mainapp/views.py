from rest_framework import viewsets, serializers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffPermission
from .models import Factory, RetailNetwork, Entrepreneur, Product
from .serializers import FactorySerializer, RetailNetworkSerializer, EntrepreneurSerializer, ProductSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated, IsStaffPermission]


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsAuthenticated, IsStaffPermission]


class EntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer
    permission_classes = [IsAuthenticated, IsStaffPermission]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsStaffPermission]
