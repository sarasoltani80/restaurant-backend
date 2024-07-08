from django.db import models
from django.utils.translation import gettext as _

class Contact(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=200)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=300)
    number = models.IntegerField(_("تعداد") , default=1)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.email

