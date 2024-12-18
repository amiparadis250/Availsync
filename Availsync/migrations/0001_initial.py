# Generated by Django 5.1.3 on 2024-11-25 04:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('totalstuffs', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bio', models.CharField(max_length=200)),
                ('working_days', models.CharField(max_length=200)),
                ('working_hours', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'institutions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('profile_image', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('profile_image', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('workdescription', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Availsync.institution')),
            ],
            options={
                'db_table': 'staffs',
            },
        ),
    ]
