# Generated by Django 3.2.5 on 2021-07-21 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transactions_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='unit_price',
            field=models.FloatField(editable=False, null=True, verbose_name='Preço unitário'),
        ),
    ]
