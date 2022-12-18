# Generated by Django 4.1.3 on 2022-11-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_alter_calendar_calendar_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='calendar_holiday',
            field=models.TextField(choices=[('0', '平日'), ('1', '休日')], default='平日', max_length=1, verbose_name='休日'),
        ),
    ]
