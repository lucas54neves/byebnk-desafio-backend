from rest_framework import serializers
from assets import models

class AssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Assets
    fields = '__all__'