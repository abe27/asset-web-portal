from django.contrib import admin

from .models import AssetType, StockAsset, Supplier

# Register your models here.
# Register your models here.
class AssetTypeAdmin(admin.ModelAdmin):
    list_filter = [
        "is_active",
        "created_at",
        "updated_at",
    ]
    search_fields = ["name"]
    list_display = [
        "name",
        "description",
        "is_active",
        "created_at",
    ]
    list_per_page = 15
    pass


class SupplierAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "address",
                    (
                        "tel_no",
                        "email",
                    ),
                    "description",
                )
            },
        ),
    )

    list_filter = [
        "is_active",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "name",
        "address",
        "tel_no",
        "email",
        "description",
    ]
    list_display = [
        "name",
        "address",
        "tel_no",
        "email",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_per_page = 15
    pass


class StockAssetAdmin(admin.ModelAdmin):
    list_filter = [
        "is_active",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "asset_type",
        "name",
    ]
    list_display = [
        "asset_type",
        "name",
        "description",
        "qty",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_per_page = 15
    pass

admin.site.register(AssetType, AssetTypeAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(StockAsset, StockAssetAdmin)