# Generated by Django 5.0.1 on 2024-03-04 07:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='authority',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=700, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='منتشر شده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='تغییر یافته'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='پرداخت شده؟'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.CharField(blank=True, max_length=700, verbose_name='یادداشت سفارش'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]