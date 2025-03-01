# Generated by Django 5.0.4 on 2024-05-05 23:56

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_products_sku_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Sku',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('sku', models.CharField(max_length=450)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('color_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.product_attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('size_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size', to='shop.product_attribute')),
            ],
        ),
        migrations.DeleteModel(
            name='Products_Sku',
        ),
    ]
