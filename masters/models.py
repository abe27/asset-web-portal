from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
today = timezone.now

# Create your models here.
NETWORK_CHOICE = (
    ("0", "-"),
    ("1", "DHCP"),
    ("2", "Static IP"),
)

class AssetType(models.Model):### Product TAG
    name = models.CharField(max_length=255, verbose_name=_("ชื่อประเภทสินทรัพย์"))
    description = models.TextField(verbose_name=_("รายละเอียด"), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "tbt_asset_type"
        verbose_name = _("ประเภทสินทรัพย์")
        verbose_name_plural = _("ประเภทสินทรัพย์")

class Supplier(models.Model):### partner
    name = models.CharField(max_length=255, verbose_name=_("ชื่อผู้ผลิต"))
    address = models.TextField(verbose_name=_("ที่อยู่"), blank=True, null=True)
    tel_no = models.CharField(max_length=25, verbose_name=_("เบอร์โทรศัพท์"), blank=True, null=True)
    email = models.EmailField(verbose_name=_("อีเมล์"), blank=True, null=True)
    description = models.TextField(verbose_name=_("รายละเอียด"), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "tbt_supplier"
        verbose_name = _("บริษัทจัดจำหน่าย")
        verbose_name_plural = _("บริษัทจัดจำหน่าย")

class StockAsset(models.Model):### Inventory
    asset_type = models.ForeignKey(AssetType, verbose_name=_("ประเภทสินทรัพย์"), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_("ชื่อสินทรัพย์"))
    description = models.TextField(verbose_name=_("รายละเอียด"), blank=True, null=True)
    qty = models.IntegerField(verbose_name=_("จำนวนคงเหลือ"), blank=True, null=True,default="0")
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "tbt_stock_asset"
        verbose_name = _("คลังสินทรัพย์")
        verbose_name_plural = _("คลังสินทรัพย์")