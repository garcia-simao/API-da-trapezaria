from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Usuario, Funcionario, Prato_do_dia, Avaliacao_da_cozinha, Avaliacao_de_alimentos, Infomacao_de_tempetatura
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

class CoreTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testeuser1',
            password='1234',
            email='teste@gmail.com'
        )

        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    # Seus casos de teste devem ser adicionados aqui
