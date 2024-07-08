from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Blog(models.Model):
    title = models.CharField(_("عنوان") , max_length=50)
    description = models.CharField(_("توضیحات") , max_length=200)
    content = models.TextField(_("متن"))
    created_at = models.DateTimeField(_("زمان انتشار") , default=timezone.now)
    author = models.ForeignKey(User , verbose_name= _("نویسنده") , on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر") , upload_to="blogs/" , blank=True , null=True)
    category = models.ForeignKey("Category", verbose_name=_("دسته بندی") , related_name="blog" ,on_delete=models.CASCADE , blank=True,null=True)
    Tag = models.ManyToManyField("Tag" , verbose_name=_("تگ ها") , related_name= "blog")

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(_("عنوان") , max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار") , auto_now=False , auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار") , auto_now=False , auto_now_add=True)
    updated_at = models.DateTimeField(_("تاریخ بروزرسانی") , auto_now=True , auto_now_add= False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey("Blog" , verbose_name=_("مقاله") , related_name='comments' , on_delete=models.CASCADE)
    name = models.CharField( _("نام"), max_length=500)
    email = models.EmailField(_("آدرس_الکترونیکی") , max_length=256)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=False , auto_now_add=True)

    def __str__(self):
        return self.email

