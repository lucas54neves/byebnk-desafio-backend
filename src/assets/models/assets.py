from django.db import models
from uuid import uuid4

class Assets(models.Model):
  class AssetType(models.TextChoices):
    CRIPTO = 'CR', 'Cripto'
    VARIABLE = 'RV', 'Renda variavel'
    FIXED = 'RF', 'Renda fixa'

  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField('Nome', max_length=255)
  modality = models.CharField('Modalidade', max_length=2, choices=AssetType.choices, default=AssetType.FIXED)
  value = models.FloatField('Valor')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Atualizado em', auto_now=True)