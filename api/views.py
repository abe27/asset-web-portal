from rest_framework import viewsets
from .serializers import AssetTypeSerializer, StockAssetSerializer, SupplierSerializer
from masters.models import AssetType, Supplier,StockAsset

class AssetTypeViewSet(viewsets.ModelViewSet):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class StockAssetViewSet(viewsets.ModelViewSet):
    queryset = StockAsset.objects.all()
    serializer_class = StockAssetSerializer

