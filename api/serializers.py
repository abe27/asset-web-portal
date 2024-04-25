from rest_framework import serializers
from masters.models import AssetType

class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = "__all__"