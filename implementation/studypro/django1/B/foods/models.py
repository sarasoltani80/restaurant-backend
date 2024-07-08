from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class food(models.Model):
    FOOD_TYPE=[
        ("Breakfast" , "صبحانه"),
        ("lunch" , "ناهار"),
        ("drinks" , "نوشیدنی"),
        ("dinner" , "شام"),
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(_("توضیحات") , max_length=50)
    rate = models.IntegerField(_("امتیاز") , default=0)
    price = models.IntegerField(_("قیمت"))
    time = models.IntegerField(_("زمان لازم"))
    pub_date = models.DateField(_("تاریخ انتشار") , auto_now=False , auto_now_add=True)
    photo = models.ImageField(upload_to='foods/' , height_field=None , width_field= None , max_length= None)
    type_food = models.CharField(_("نوع غذا") , max_length=10 , choices= FOOD_TYPE , default="drinks")

    def __str__(self):
        return self.name


class Sabad(models.Model):
    user = models.ForeignKey(User, verbose_name=_("کاربر"), related_name="sabad", on_delete=models.CASCADE, null=True)
    food = models.ForeignKey("food", verbose_name=_("غذاها"), related_name="sabad", on_delete=models.CASCADE , null=True)
    created_at = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    number = models.IntegerField(_("تعداد"), default=1)
    total_price = models.IntegerField(_("تعداد"), default=0)
    Is_final = models.BooleanField(_("پرداخت شده یا نشده") , default=False)
    order_number = models.CharField(_("شماره سفارش") , default="-1" , max_length=800)

    #def __str__(self):
     #   return self.user

class Wallet(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    money = models.BigIntegerField(_("موجودی حساب") , default=0)

class Vote(models.Model):
    user = models.ForeignKey(User, verbose_name=_("کاربر"), related_name="vote", on_delete=models.CASCADE, null=True)
    food = models.ForeignKey("food", verbose_name=_("غذاها"), related_name="vote", on_delete=models.CASCADE, null=True)
    price_rate = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    behdasht_rate = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    service_rate = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
