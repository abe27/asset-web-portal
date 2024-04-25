from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'asset_type', views.AssetTypeViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'stock_asset', views.StockAssetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]