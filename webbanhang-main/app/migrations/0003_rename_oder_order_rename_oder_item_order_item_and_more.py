# Generated by Django 5.0.7 on 2024-08-03 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Oder_Item',
            new_name='Order_Item',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_oder',
            new_name='date_order',
        ),
        migrations.RenameField(
            model_name='order_item',
            old_name='oderr',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='oderr',
            new_name='order',
        ),
    ]
