# Generated by Django 3.2.5 on 2021-07-22 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_alter_transactions__unit_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='_unit_price',
        ),
    ]
