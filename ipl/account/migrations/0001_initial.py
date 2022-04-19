# Generated by Django 3.2 on 2021-12-16 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPLUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('created_dtm', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is Superuser?')),
            ],
            options={
                'db_table': 'users',
                'get_latest_by': 'created_dtm',
            },
        ),
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('reset_key', models.UUIDField()),
                ('created_dtm', models.DateTimeField(auto_now_add=True)),
                ('updated_dtm', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'passwords',
                'get_latest_by': 'created_dtm',
            },
        ),
    ]
