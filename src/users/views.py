from rest_framework import viewsets
from users import serializers, models
from django.http import HttpResponse, JsonResponse

class UserViewSet(viewsets.ModelViewSet):
  def balance(self):
    response_data = {}
    response_data['balance'] = self.user.balance
    return JsonResponse(response_data)