from rest_framework import viewsets
from .serializers import AssetTypeSerializer
from masters.models import AssetType

class AssetTypeViewSet(viewsets.ModelViewSet):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer