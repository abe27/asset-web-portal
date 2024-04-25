from rest_framework import serializers
from masters.models import AssetType, Supplier, StockAsset

class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

class StockAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockAsset
        fields = "__all__"
