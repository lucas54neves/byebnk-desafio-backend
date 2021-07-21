from django.test import TestCase
from assets.models import Assets

class AssetTestCase(TestCase):
  def setUp(self):
    self.asset = Assets.objects.create(
      name='Bitcoin',
      modality='CR',
      value=120
    )
  
  def test_get(self):
    asset = Assets.objects.get(pk=self.asset.id)

    self.assertEqual(asset.name, 'Bitcoin')
    self.assertEqual(asset.modality, 'CR')
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

