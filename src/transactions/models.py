from django.db import models
from uuid import uuid4
from assets.models import Assets
from users.models import User

class Transactions(models.Model):
  class TransactionType(models.TextChoices):
    APPLICATION = 'AP', 'Aplicação'
    RESCUE = 'RE', 'Resgate'
  
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  asset = models.ForeignKey(Assets, verbose_name='Ativo', on_delete=models.PROTECT)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  type = models.CharField('Tipo', max_length=2, choices=TransactionType.choices, default=TransactionType.APPLICATION)
  date = models.DateTimeField('Data de transação')
  quantity = models.IntegerField('Quantidade')
  unit_price = models.FloatField('Preço unitário')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Atualizado em', auto_now=True)