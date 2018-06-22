# Generated by Django 2.0.6 on 2018-06-22 03:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('flag', models.URLField(blank=True, max_length=100, null=True, unique=True)),
                ('currency', models.CharField(max_length=3, unique=True)),
                ('iso_code', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
