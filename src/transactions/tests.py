from django.test import TestCase
from datetime import datetime, timezone
from transactions.models import Transactions
from assets.models import Assets
from users.models import User

class AssetTestCase(TestCase):
  def setUp(self):
    self.date_now = datetime.now(timezone.utc)

    self.user = User.objects.create(
      username='user',
      password='123456'
    )

    self.asset = Assets.objects.create(
      name='Bitcoin',
      modality='cripto',
      value=120
    )

    self.transaction = Transactions.objects.create(
      type='application',
      date=self.date_now,
      quantity=26,
      asset=self.asset,
      ip_address='127.0.0.1',
      user_id=self.user.id
    )
  
  def test_get(self):
    transaction = Transactions.objects.get(pk=self.transaction.id)

    self.assertEqual(transaction.type, 'application')
    self.assertEqual(transaction.date, self.date_now)
    self.assertEqual(transaction.quantity, 26)
    self.assertEqual(transaction.asset.id, self.asset.id)
    self.assertEqual(transaction.ip_address, '127.0.0.1')
    self.assertEqual(transaction.user_id, self.user.id)


