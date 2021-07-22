# Generated by Django 3.2.5 on 2021-07-22 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_remove_transactions__unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='unit_price',
            field=models.FloatField(editable=False, null=True, verbose_name='Preço unitário'),
        ),
    ]