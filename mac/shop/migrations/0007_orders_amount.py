# Generated by Django 4.2.4 on 2023-09-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_ordersupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
