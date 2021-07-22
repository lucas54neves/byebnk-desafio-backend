from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User

class UserAPITestCase(APITestCase):
  def test_signup(self):
    response = self.client.post('/accounts/signup', {
      'email':'test@mail.com',
      'password': '123',
    }, format='json')

    self.assertRedirects(response, '/accounts/signup/', status_code=301, target_status_code=200)
  
  def test_login(self):
    User.objects.create(
      email='test@mail.com',
      password='123456'
    )

    response = self.client.post('/accounts/login', {
      'email':'test@mail.com',
      'password': '123',
    }, format='json')

    self.assertRedirects(response, '/accounts/login/', status_code=301, target_status_code=200)

  def test_logout(self):
    user = User.objects.create(
      email='test@mail.com',
      password='123456'
    )
    
    self.client.force_authenticate(user=user)

    response = self.client.post('/accounts/logout/', {'revoke_token': 'false'}, format='json')
    
    self.assertEqual(response.status_code, 200)
    