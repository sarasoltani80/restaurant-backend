# Generated by Django 4.2.3 on 2023-07-29 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_alter_reservation_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserve', to='reservation.table', verbose_name='میز انتخابی'),
        ),
    ]