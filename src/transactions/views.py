from rest_framework import viewsets
from transactions.models import Transactions
from transactions.serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
  #permission_classes = (IsAuthenticated, )
  serializer_class = TransactionSerializer
  queryset = Transactions.objects.all()