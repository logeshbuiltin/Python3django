# Generated by Django 3.2 on 2021-12-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20211217_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingordersmodel',
            name='freight_charges',
            field=models.FloatField(default=0),
        ),
    ]
