# Generated by Django 3.2 on 2021-12-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipluser',
            name='is_secondaryUser',
            field=models.BooleanField(default=False),
        ),
    ]
