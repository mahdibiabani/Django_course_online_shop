# Generated by Django 5.0.1 on 2024-02-19 07:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_short_description_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Time of modification'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Product Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Product Short Descriptions'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Product Title'),
        ),
    ]
