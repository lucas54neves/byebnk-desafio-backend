# Generated by Django 3.2.5 on 2021-07-21 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_alter_assets_modality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='value',
            field=models.FloatField(editable=False, verbose_name='Valor'),
        ),
    ]