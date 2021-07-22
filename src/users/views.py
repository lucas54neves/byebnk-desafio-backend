from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from users import serializers, models

class UserViewSet(viewsets.ModelViewSet):
  def balance(self):
    try:
      response_data = {}
      response_data['balance'] = self.user.balance
      return JsonResponse(response_data)
    except:
      return JsonResponse({
        'message': 'Apenas usuários autenticados podem visualizar o saldo.'
      },
      status=403)
      