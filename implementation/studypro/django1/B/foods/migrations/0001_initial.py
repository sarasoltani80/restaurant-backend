# Generated by Django 4.2.3 on 2023-07-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50, verbose_name='توضیحات')),
                ('rate', models.IntegerField(verbose_name='امتیاز')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('time', models.IntegerField(verbose_name='زمان لازم')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('photo', models.ImageField(upload_to='foods/')),
            ],
        ),
    ]