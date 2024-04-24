from django.contrib import admin
from .models import Accessories, Asset


class AccessoriesAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "asset_type",
                        "supplier",
                    ),
                    "receive_date",
                    "name",
                    "description",
                )
            },
        ),
        (
            "Detail",
            {
                "classes": ("collapse",),
                "fields": (
                    (
                        "serial_no",
                        "asset_no",
                    )
                ),
            },
        ),
        (
            "Warranty",
            {
                "classes": ("collapse",),
                "fields": (
                    "on_year",
                    (
                        "warranty_year",
                        "warranty_month",
                    ),
                    (
                        "warranty_from",
                        "warranty_to",
                    ),
                ),
            },
        ),
        (
            "Attachment",
            {
                "classes": ("collapse",),
                "fields": ("asset_pic",),
            },
        ),
        (
            None,
            {
                "fields": ("is_active",),
            },
        ),
    )

    list_filter = [
        "asset_type",
        "is_active",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "name",
        "serial_no",
        "asset_no",
    ]
    list_display = [
        "asset_type",
        "supplier",
        "receive_date",
        "name",
        "description",
        "serial_no",
        "asset_no",
        "on_year",
        "warranty_year",
        "warranty_month",
        "warranty_from",
        "warranty_to",
        "asset_pic",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_per_page = 15
    pass

class AssetAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "accessories",
                        "employee",
                    ),
                    (
                        "cpu_type",
                        "cpu_count",
                    ),
                    "ram_size",
                    (
                        "hdd_size",
                        "sdd_size",
                    ),
                    (
                        "monitor_type",
                        "monitor_size",
                    ),
                    "description",
                    "is_active",
                )
            },
        ),
        (
            "Network Interface",
            {
                "classes": ("collapse",),
                "fields": (
                    (
                        "port_lan",
                        "wire_lan",
                    ),
                    "network_type",
                    (
                        "ip_address",
                        "mac_address",
                    ),
                ),
            },
        ),
    )
    list_filter = [
        "is_active",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "accessories",
        "employee",
        "cpu_type",
        "cpu_count",
        "ram_size",
        "hdd_size",
        "sdd_size",
        "monitor_type",
        "monitor_size",
        "ip_address",
        "mac_address",
    ]
    list_display = [
        "accessories",
        "employee",
        "cpu_type",
        "cpu_count",
        "ram_size",
        "hdd_size",
        "sdd_size",
        "monitor_type",
        "monitor_size",
        "port_lan",
        "wire_lan",
        "network_type",
        "ip_address",
        "mac_address",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    ]

    list_per_page = 15
    pass

admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Asset, AssetAdmin)
