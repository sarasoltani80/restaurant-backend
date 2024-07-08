from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone


class Table(models.Model):
    location = models.CharField(_("لوکیشن"), max_length=500)
    chairsnumber = models.IntegerField(_("تعداد صندلی ها"), default=2)
    category = models.CharField(_("فضای اطراف میز"), max_length=500)
    photo = models.ImageField(upload_to='tables/', height_field=None, width_field=None, max_length=None)

    #def __str__(self):
     #   return self.location

class Reservation(models.Model):
    DURATION_TYPE = [
        ("30", "نیم ساعت"),
        ("60", "یک ساعت"),
    ]

    user = models.ForeignKey(User , verbose_name= _("مشتری") , related_name='reservation' , on_delete=models.CASCADE , null=True)
    table = models.ForeignKey("Table" , verbose_name=_("میز انتخابی") , related_name='reservation' , on_delete=models.CASCADE , null=True)
    phone = models.CharField(_("شماره تلفن") , max_length=20)
    number = models.IntegerField(_("تعداد"))
    date = models.DateField(_("تاریخ") , auto_now=False , auto_now_add=False)
    start_time = models.TimeField(_("زمان شروع") , auto_now=False , auto_now_add=False , null=True)
    final_time = models.TimeField(_("زمان پایان") , auto_now=False , auto_now_add=False , null=True)
    duration = models.CharField(_("مدت زمان رزرو") , choices=DURATION_TYPE , default="30" , max_length=50)


    def __str__(self):
        return self.phone



