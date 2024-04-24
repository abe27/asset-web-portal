from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
today = timezone.now

from masters.models import AssetType, Supplier
from users.models import UserModel

# Create your models here.
NETWORK_CHOICE = (
    ("0", "-"),
    ("1", "DHCP"),
    ("2", "Static IP"),
)

class Accessories(models.Model):
    asset_type = models.ForeignKey(AssetType, verbose_name=_("ประเภทสินทรัพย์"), on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, verbose_name=_("บริษัทจัดจำหน่าย"), on_delete=models.CASCADE)
    receive_date = models.DateField(verbose_name=_("วันทีรับเข้าระบบ"), blank=True, null=True, default=today)
    name = models.CharField(max_length=255, verbose_name=_("ชื่อสินทรัพย์/ยี่ห้อรุ่น"))
    description = models.TextField(verbose_name=_("รายละเอียด"), blank=True, null=True)
    serial_no = models.CharField(max_length=50, verbose_name=_("หมายเลข Serial No."))
    asset_no = models.CharField(max_length=50, verbose_name=_("หมายเลขทรัพย์สิน"), blank=True, null=True)
    on_year = models.IntegerField(verbose_name=_("ปีที่สั่งซื้อ"), blank=True, null=True,default="0")
    warranty_year = models.IntegerField(verbose_name=_("การรับประกัน/ปี"), blank=True, null=True,default="0")
    warranty_month = models.IntegerField(verbose_name=_("การรับประกัน/เดือน"), blank=True, null=True,default="0")
    warranty_from = models.DateField(verbose_name=_("วันที่เริ่มรับประกัน"), blank=True, null=True)
    warranty_to = models.DateField(verbose_name=_("วันที่สินสุดรับประกัน"), blank=True, null=True)
    asset_pic = models.ImageField(verbose_name=_("รูปภาพประกอบ"), upload_to="static/assets/",blank=True,null=True)
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "tbt_accessories"
        verbose_name = _("รายการอุปกรณ์")
        verbose_name_plural = _("รายการอุปกรณ์")


class Asset(models.Model):
    accessories = models.ForeignKey(Accessories, verbose_name=_("รายการอุปกรณ์"), on_delete=models.CASCADE,blank=True)
    employee = models.ForeignKey(UserModel, verbose_name=_("ผู้ใช้งาน"),on_delete=models.CASCADE,blank=True)
    cpu_type = models.CharField(max_length=255, verbose_name=_("รุ่น CPU"),blank=True, null=True,default="-")
    cpu_count= models.FloatField(verbose_name=_("ขนาด CPU/GB"),blank=True, null=True,default="0")
    ram_size = models.FloatField(verbose_name=_("ขนาด RAM/GB"), blank=True, null=True, default="4")
    hdd_size = models.CharField(max_length=255,verbose_name=_("ขนาด HDD/GB/TB"), blank=True, null=True, default="-")
    sdd_size = models.CharField(max_length=255,verbose_name=_("ขนาด SSD/GB/TB"), blank=True, null=True, default="-")
    monitor_type = models.CharField(max_length=255, verbose_name=_("รุ่น Monitor"),blank=True, null=True,default="-")
    monitor_size = models.CharField(max_length=255, verbose_name=_("ขนาดหน้าจอ"),blank=True, null=True,default="-")
    port_lan = models.BooleanField(verbose_name=_("Port Lan"), blank=True, null=True, default=True)
    wire_lan = models.BooleanField(verbose_name=_("Wireless Lan"), blank=True, null=True, default=False)
    network_type = models.CharField(max_length=1, verbose_name=_("รูปแบบ IP Address"), choices=NETWORK_CHOICE, blank=True, null=True,default="0")
    ip_address = models.GenericIPAddressField(verbose_name=_("หมายเลข IP Address"), blank=True, null=True)
    mac_address = models.CharField(max_length=50, verbose_name=_("MAC Address"), blank=True, null=True)
    description = models.TextField(verbose_name=_("หมายเหตุ"), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "tbt_asset"
        verbose_name = _("รายการสินทรัพย์")
        verbose_name_plural = _("รายการสินทรัพย์")