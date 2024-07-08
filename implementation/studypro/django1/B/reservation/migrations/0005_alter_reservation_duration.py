# Generated by Django 4.2.3 on 2023-07-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_alter_reservation_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='duration',
            field=models.CharField(choices=[('30', 'نیم ساعت'), ('60', 'یک ساعت')], default='30', max_length=50, verbose_name='مدت زمان رزرو'),
        ),
    ]