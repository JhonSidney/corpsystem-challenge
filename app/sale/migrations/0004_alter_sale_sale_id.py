# Generated by Django 4.2.11 on 2024-03-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_alter_sale_payment_methods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]