# Generated by Django 3.2 on 2021-12-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20211216_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='actual_weight',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='charged_weight',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='door_collection',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='door_delivery',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='freight_charges',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='hamali_charges',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='lr_charges',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='other_charges',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='paid_amount',
            field=models.FloatField(default=None, null=True),
        ),
    ]
