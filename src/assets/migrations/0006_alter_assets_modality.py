# Generated by Django 3.2.5 on 2021-07-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_alter_assets_modality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='modality',
            field=models.CharField(choices=[('CR', 'Cripto'), ('RV', 'Renda variavel'), ('RF', 'Renda fixa')], default='RF', max_length=2, verbose_name='Modalidade'),
        ),
    ]
