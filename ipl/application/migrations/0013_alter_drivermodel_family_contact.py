# Generated by Django 3.2 on 2021-12-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20211219_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivermodel',
            name='family_contact',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
    ]