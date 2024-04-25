from rest_framework import viewsets
from .serializers import (
    AssetTypeSerializer,
    CompanySerializer,
    DepartmentSerializer,
    PositionSerializer,
    SectionSerializer,
    StockAssetSerializer,
    SupplierSerializer,
    UserModelSerializer,
    AccessoriesSerializer,
    AssetSerializer,
)
from masters.models import AssetType, Supplier, StockAsset
from users.models import Position, Department, Section, Company, UserModel
from assets.models import Accessories, Asset


class AssetTypeViewSet(viewsets.ModelViewSet):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class StockAssetViewSet(viewsets.ModelViewSet):
    queryset = StockAsset.objects.all()
    serializer_class = StockAssetSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class AccessoriesViewSet(viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer