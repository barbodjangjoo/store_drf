# Generated by Django 5.1.2 on 2025-01-03 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='address', serialize=False, to='store.customer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discounts',
            field=models.ManyToManyField(blank=True, related_name='discounts', to='store.discount'),
        ),
    ]
