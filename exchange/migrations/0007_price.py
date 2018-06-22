# Generated by Django 2.0.6 on 2018-06-22 20:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0006_auto_20180622_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('btc_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('ltc_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('eth_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('bch_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchange', to='exchange.Exchange')),
            ],
        ),
    ]