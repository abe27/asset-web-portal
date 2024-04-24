from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
MEMBER_LEVEL_CHOICES = (
    ("0", _("User")),
    ("1", _("Staff")),
    ("2", _("Manager")),
)

GENDER_CHOICES = (
    ("0", _("Male")),
    ("1", _("Female")),
    ("2", _("Other")),
)


class Position(models.Model):
    name = models.CharField(
        verbose_name=_("หัวข้อ"), max_length=255, unique=True, blank=False, null=False
    )
    description = models.TextField(verbose_name=_("รายละเอียด"), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbt_position"
        verbose_name = _("ตำแหน่ง")
        verbose_name_plural = _("ตำแหน่ง")


class Department(models.Model):
    name = models.CharField(
        verbose_name=_("หัวข้อ"), max_length=255, unique=True, blank=False, null=False
    )
    description = models.TextField(verbose_name=_("รายละเอียด"), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbt_department"
        verbose_name = _("แผนก")
        verbose_name_plural = _("แผนก")


class Section(models.Model):
    name = models.CharField(
        verbose_name=_("หัวข้อ"), max_length=255, unique=True, blank=False, null=False
    )
    description = models.TextField(verbose_name=_("รายละเอียด"), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbt_section"
        verbose_name = _("ฝ่าย")
        verbose_name_plural = _("ฝ่าย")


class Company(models.Model):
    name = models.CharField(
        verbose_name=_("หัวข้อ"), max_length=255, unique=True, blank=False, null=False
    )
    description = models.TextField(verbose_name=_("รายละเอียด"), blank=True, null=True)
    domain_name = models.CharField(
        verbose_name=_("โดเมนเนม"), max_length=255, blank=True, null=True, default="-"
    )
    domain_mail = models.CharField(
        verbose_name=_("โดเมนอีเมล์"), max_length=255, blank=True, null=True, default="-"
    )
    is_active = models.BooleanField(verbose_name=_("สถานะ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbt_company"
        verbose_name = _("บริษัท")
        verbose_name_plural = _("บริษัท")


class UserModel(AbstractUser):
    employee_code = models.CharField(verbose_name=_("รหัสพนักงาน"), max_length=15)
    member_level = models.CharField(verbose_name=_("ลำดับ"), max_length=1, choices=MEMBER_LEVEL_CHOICES)
    mobile_no = models.CharField(
        verbose_name=_("เบอร์มือถือ"), max_length=25, blank=True, null=True, default="-"
    )
    tel_no = models.CharField(
        verbose_name=_("เบอร์โทร"), max_length=25, blank=True, null=True, default="-"
    )
    position_id = models.ForeignKey(Position, verbose_name=_("ตำแหน่ง"),on_delete=models.SET_NULL, null=True)
    depart_id = models.ForeignKey(Department, verbose_name=_("แผนก"),on_delete=models.SET_NULL, null=True)
    section_id = models.ForeignKey(Section, verbose_name=_("ฝ่าย/ส่วน"),on_delete=models.SET_NULL, null=True)
    company_id = models.ForeignKey(Company, verbose_name=_("บริษัท"),on_delete=models.SET_NULL, null=True)
    avatar_img = models.ImageField(verbose_name=_("รูปประจำตัว"),upload_to="static/uploads/users/avatars/")
    signature_img = models.ImageField(verbose_name=_("ลายเซนต์"),upload_to="static/uploads/users/signatures/")
    gender = models.CharField(max_length=1, verbose_name=_("เพศ"),choices=GENDER_CHOICES, default="M")
    is_active = models.BooleanField(verbose_name=_("ปิด/เปิด"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tbt_employees"
        verbose_name = _("ผู้ใช้งาน")
        verbose_name_plural = _("ผู้ใช้งาน")
        ordering = ["-created_at"]
