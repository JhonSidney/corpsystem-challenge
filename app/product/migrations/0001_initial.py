# Generated by Django 4.2.11 on 2024-03-16 20:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]


    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('stock_quantity', models.IntegerField()),
            ],
        ),
    ]
