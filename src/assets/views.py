from rest_framework import viewsets
from assets import serializers, models

class AssetViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.AssetSerializer
  queryset = models.Assets.objects.all()