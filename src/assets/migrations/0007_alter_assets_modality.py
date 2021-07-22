# Generated by Django 3.2.5 on 2021-07-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_alter_assets_modality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='modality',
            field=models.CharField(choices=[('cripto', 'Cripto'), ('variable', 'Renda variavel'), ('fixed', 'Renda fixa')], default='fixed', max_length=25, verbose_name='Modalidade'),
        ),
    ]