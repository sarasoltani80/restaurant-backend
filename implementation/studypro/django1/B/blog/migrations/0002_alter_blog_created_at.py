# Generated by Django 4.2.3 on 2023-07-11 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
    ]
