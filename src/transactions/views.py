from rest_framework import viewsets
from transactions.serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from transactions.models import Transactions
from users.models import User
from assets.models import Assets

class TransactionViewSet(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated, )
  serializer_class = TransactionSerializer

  def get_queryset(self):
    return [transaction for transaction in Transactions.objects.all() if transaction.user.id == self.request.user.id]

  def get_object(self):
    return get_object_or_404(Transactions, pk=self.kwargs['pk'])
  
  def update(self, request, pk=None):
    return Response('Não é permitido editar transações', status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, *args, **kwargs):
    return Response('Não é permitido remover transações', status=status.HTTP_400_BAD_REQUEST)
  
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if request.method == 'POST':
      if serializer.is_valid():
        user = User.objects.get(id=request.user.id)

        asset = Assets.objects.get(id=self.request.POST.get('asset'))

        if (request.POST.get('type') == 'application'):
          user.balance += asset.value * int(request.POST.get('quantity'))
          # Taxa de custodia para renda fixa = $ 2.5
          # Taxa de custodia para renda variavel = $ 0.0
          # Taxa de custodia para criptos = $ 5.0
          # Taxa de administracao para renda fixa = 0.5%
          # Taxa de administracao para renda variavel = 0.25%
          # Taxa de administracao para criptos = 0.75%
          if asset.modality == 'fixed':
            user.balance -= 2.5
            user.balance *= 0.005
          elif asset.modality == 'variable':
            user.balance *= 0.0025
          elif asset.modality == 'cripto':
            user.balance -= 2.5
            user.balance *= 0.0075

        if (request.POST.get('type') == 'rescue'):
          # Tarifa de saque = 0.25%
          user.balance *= 0.0025
        
        user.save()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

  def perform_create(self, serializer):
    asset = Assets.objects.get(id=self.request.POST.get('asset'))
    serializer.save(user=self.request.user, ip_address=self.request.META.get('REMOTE_ADDR'), unit_price=asset.value)
  