# Generated by Django 4.2.3 on 2023-07-29 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=500, verbose_name='لوکیشن')),
                ('chairsnumber', models.IntegerField(default=2, verbose_name='تعداد صندلی ها')),
                ('category', models.CharField(max_length=500, verbose_name='فضای اطراف میز')),
                ('photo', models.ImageField(upload_to='tables/')),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time',
        ),
        migrations.AddField(
            model_name='reservation',
            name='duration',
            field=models.CharField(choices=[('half an hour', 'نیم ساعت'), ('an hour', 'یک ساعت')], default='half an hour', max_length=50, verbose_name='مدت زمان رزرو'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='final_time',
            field=models.TimeField(null=True, verbose_name='زمان پایان'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='زمان شروع'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserve', to=settings.AUTH_USER_MODEL, verbose_name='مشتری'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='reservation.table', verbose_name='میز انتخابی'),
        ),
    ]