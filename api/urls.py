from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'asset_type', views.AssetTypeViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'stock_asset', views.StockAssetViewSet)
router.register(r'position', views.PositionViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'section', views.SectionViewSet)
router.register(r'company', views.CompanyViewSet)
router.register(r'user', views.UserModelViewSet)
router.register(r'accessories', views.AccessoriesViewSet)
router.register(r'asset', views.AssetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]