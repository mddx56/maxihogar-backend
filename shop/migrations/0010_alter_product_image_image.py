# Generated by Django 5.0.4 on 2024-05-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_image_product_sku_delete_products_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
