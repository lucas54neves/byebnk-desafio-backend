from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from assets import serializers, models
import yfinance as yf


class AssetViewSet(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated, )
  serializer_class = serializers.AssetSerializer

  def get_queryset(self):
    modality_filter = self.request.query_params.get('modality')
    if modality_filter != None:
      assets = [asset for asset in models.Assets.objects.all() if asset.modality == modality_filter]
    else:
      assets = models.Assets.objects.all()

    for asset in assets:
      try:
        ticket = yf.Ticker(asset.name)

        asset.value = ticket.history(period='1d')['Close'][0]

        asset.save()
      except:
        pass
    
    return assets

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if request.method == 'POST':
      if serializer.is_valid():
        try:
          self.perform_create(serializer)
        except Exception as error:
          return Response(error.args, status=status.HTTP_400_BAD_REQUEST)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)
  
  def perform_create(self, serializer):
    try:
      ticket = yf.Ticker(self.request.POST.get('name'))

      price = ticket.history(period='1d')['Close'][0]
    except:
      raise Exception('Nome do ativo inválido.')

    serializer.save(value=price)
  