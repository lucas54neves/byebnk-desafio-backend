from django.db import models
from uuid import uuid4
import yfinance as yf

class Assets(models.Model):
  class AssetType(models.TextChoices):
    CRIPTO = 'cripto', 'Cripto'
    VARIABLE = 'variable', 'Renda variavel'
    FIXED = 'fixed', 'Renda fixa'

  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField('Nome', max_length=255)
  modality = models.CharField('Modalidade', max_length=25, choices=AssetType.choices, default=AssetType.FIXED)
  value = models.FloatField('Valor',  editable=False)
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Atualizado em', auto_now=True)

  def __str__(self):
    return self.name[:30]

  def get_value(self):
    ticket = yf.Ticker(self.name)

    return ticket.history(period='1d')['Close'][0]