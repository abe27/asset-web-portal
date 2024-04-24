from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserModel, Position, Department, Section, Company


# Register your models here.


class PositionAdmin(admin.ModelAdmin):
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
        "updated_at",
    ]
    list_per_page = 15
    pass


class DepartmentAdmin(admin.ModelAdmin):
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
        "updated_at",
    ]
    list_per_page = 15
    pass


class SectionAdmin(admin.ModelAdmin):
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
        "updated_at",
    ]
    list_per_page = 15
    pass


class CompanyAdmin(admin.ModelAdmin):
    list_filter = [
        "is_active",
        "created_at",
        "updated_at",
    ]
    search_fields = ["name"]
    list_display = [
        "name",
        "description",
        "domain_name",
        "domain_mail",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_per_page = 15
    pass


class UserAdmin(BaseUserAdmin):
    list_filter = [
        "is_active",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "email",
        "first_name",
        "last_name",
        "mobile_no",
        "tel_no",
    ]
    list_display = [
        "email",
        "first_name",
        "last_name",
        "mobile_no",
        "tel_no",
        # "position_id",
        # "depart_id",
        # "section_id",
        "company_id",
        "is_staff",
        "is_superuser",
        "is_active",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            ("Personal info"),
            {
                "classes": ("wide",),
                "fields": (
                    "employee_code",
                    (
                        "first_name",
                        "last_name",
                    ),
                    "gender",
                    (
                        "mobile_no",
                        "tel_no",
                    ),
                    (
                        "position_id",
                        "depart_id",
                    ),
                    (
                        "section_id",
                        "company_id",
                    ),
                    "member_level",
                ),
            },
        ),
        (
            ("Attachments"),
            {
                "classes": ("collapse",),
                "fields": (
                    "avatar_img",
                    "signature_img",
                ),
            },
        ),
        (
            ("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            ("Group"),
            {
                "classes": ("collapse",),
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        # (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ("email", "first_name", "last_name")
    list_per_page = 15
    pass


admin.site.register(UserModel, UserAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Company, CompanyAdmin)
