# Generated by Django 4.2.3 on 2023-07-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('Breakfast', 'صبحانه'), ('lunch', 'ناهار'), ('drinks', 'نوشیدنی'), ('dinner', 'شام')], default='drinks', max_length=10, verbose_name='نوع غذا'),
        ),
        migrations.AlterField(
            model_name='food',
            name='rate',
            field=models.IntegerField(default=0, verbose_name='امتیاز'),
        ),
    ]
