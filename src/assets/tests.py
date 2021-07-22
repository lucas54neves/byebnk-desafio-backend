from rest_framework.test import APITestCase
from django.test import TestCase
from assets.models import Assets
from users.models import User

class AssetTestCase(TestCase):
  def setUp(self):
    self.asset = Assets.objects.create(
      name='BTC-USD',
      modality='cripto',
      value=120
    )
  
  def test_get(self):
    asset = Assets.objects.get(pk=self.asset.id)

    self.assertEqual(asset.name, 'BTC-USD')
    self.assertEqual(asset.modality, 'cripto')
    self.assertEqual(asset.value, 120)
  
  def test_update(self):
    asset = Assets.objects.get(pk=self.asset.id) 

    asset.name = 'Tesouro direto'
    asset.modality = 'RV'
    asset.value = 10
    asset.save()

    asset_updated = Assets.objects.get(pk=self.asset.id)

    self.assertEqual(asset_updated.name, 'Tesouro direto')
    self.assertEqual(asset_updated.modality, 'RV')
    self.assertEqual(asset_updated.value, 10)
  
  def test_delete(self):
    asset = Assets.objects.get(pk=self.asset.id)

    asset.delete()

    with self.assertRaises(Assets.DoesNotExist):
      Assets.objects.get(pk=self.asset.id)

class AssetAPITestCase(APITestCase):
  def test_get(self):
    user = User.objects.create(
      email='test@mail.com',
      password='123456'
    )
    
    self.client.force_authenticate(user=user)

    Assets.objects.create(
      name='BTC-USD',
      modality='cripto',
      value=120
    )

    Assets.objects.create(
      name='PETR4.SA',
      modality='variable',
      value=12
    )

    Assets.objects.create(
      name='XPLG11.SA',
      modality='variable',
      value=10
    )

    response = self.client.get('/assets/', format='json')

    self.assertEqual(len(response.data), 3)
  
