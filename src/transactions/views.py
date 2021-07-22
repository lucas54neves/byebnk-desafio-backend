from rest_framework import viewsets
from transactions.serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from transactions.models import Transactions
from users.models import User
from assets.models import Assets
import yfinance as yf

class TransactionViewSet(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated, )
  serializer_class = TransactionSerializer

  def get_queryset(self):
    return [transaction for transaction in Transactions.objects.all() if transaction.user.id == self.request.user.id]
    # return Transactions.objects.all()

  def update(self, request, pk=None):
    return Response('Não é permitido editar transações', status=status.HTTP_400_BAD_REQUEST)
  
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if request.method == 'POST':
      if serializer.is_valid():
        user = User.objects.get(id=request.user.id)

        asset = Assets.objects.get(id=self.request.POST.get('asset'))

        if (request.POST.get('type') == 'application'):
          user.balance += asset.value * int(request.POST.get('quantity'))
        
        user.save()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

  def perform_create(self, serializer):
    asset = Assets.objects.get(id=self.request.POST.get('asset'))
    serializer.save(user=self.request.user, ip_address=self.request.META.get('REMOTE_ADDR'), unit_price=asset.value)
  