# Generated by Django 5.0.1 on 2024-03-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_authority_order_zarinpal_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zarinpal_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zarinpal_ref_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]