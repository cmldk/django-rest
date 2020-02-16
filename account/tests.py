from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.utils import json

"""terminalde - python manage.py test"""

class UserRegistirationTestCase(APITestCase):
    #doğru verilerle kayıt işlemi
    #şifre invalid olabilir
    #kullanıcı adı zaten kullanılmış olabilir
    #üye girişi yapıldıysa o sayfa gözükmemeli
    #token ile giriş işlemi yaptığımızda 403 hatası

    url = reverse("account:register")
    url_login = reverse("token_obtain_pair")

    def test_user_registiration(self):
        #Doğru verilerle kayıt işlemi
        data = {
            "username": "cemaldak",
            "password": "cemaldak"
        }
        response = self.client.post(self.url,data)
        self.assertEqual(201,response.status_code) #dönen değer 201se doğru demek

    def test_user_invalid_password_registiration(self):
        #invalid Password verisi ile kayıt işlemi
        data = {
            "username": "cemaldak",
            "password": "1"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_unique_name(self):
        #benzersiz isim testi
        self.test_user_registiration()
        data = {
            "username": "cemaldak",
            "password": "qdqwdqwdqwd"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)
    
    def test_user_authenticated_registiration(self):
        #session ile giriş yapmış kullanııcı sayfayı görememeli
        self.test_user_registiration()
        self.client.login(username = 'cemaldak',password='cemaldak')
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)


    def test_user_authenticated_token_registiration(self):
        #token ile giriş işlemi yaptığımızda 403 hatası
        self.test_user_registiration()
        data = {
            "username": "cemaldak",
            "password": "cemaldak"
        }
        response = self.client.post(self.url_login,data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION = "Bearer "+ token)

        response_2 = self.client.get(self.url)
        self.assertEqual(403, response_2.status_code)


class UserLogin(APITestCase):
    url_login = reverse("token_obtain_pair")

    def setUp(self):#testler çalışmadan çalışan function
        self.username = "cemaldak"
        self.password = "cemaldak"
        self.user = User.objects.create_user(username = self.username,password=self.password)

    def test_user_token(self):
        response = self.client.post(self.url_login, {'username':"cemaldak","password":"cemaldak"})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))

    def test_user_invalid_data(self):
        response = self.client.post(self.url_login, {'username': "adqwdqwd", "password": "cqwdwdqwdemaldak"})
        self.assertEqual(401, response.status_code)
    
    def test_user_empty_data(self):
        response = self.client.post(self.url_login, {'username': "", "password": ""})
        self.assertEqual(400, response.status_code)


class UserPasswordChange(APITestCase):
    #oturum açılmadan girildiğinde hata vermesi
    url = reverse("account:change-password")
    url_login = reverse("token_obtain_pair")

    def setUp(self):  # testler çalışmadan çalışan function
        self.username = "cemaldak"
        self.password = "cemaldak"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def login_with_token(self):
        data = {
            "username": "cemaldak",
            "password": "cemaldak"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_is_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(401,response.status_code)

    def test_with_valid_information(self):
        self.login_with_token()
        data = {
            "old_password":"cemaldak",
            "new_password":"2533cemal"
        }
        response = self.client.put(self.url,data)
        self.assertEqual(204,response.status_code)

    def test_with_wrong_information(self):
        self.login_with_token()
        data = {
            "old_password": "qwdqwdqwd",
            "new_password": "dqwdqwdqwd123"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_with_empty_information(self):
        self.login_with_token()
        data = {
            "old_password": "",
            "new_password": ""
        }
        response = self.client.put(self.url, data)
        self.assertEqual(400, response.status_code)

class UserProfileUpdate(APITestCase):
    url = reverse("account:me")
    url_login = reverse("token_obtain_pair")

    def setUp(self):  # testler çalışmadan çalışan function
        self.username = "cemaldak"
        self.password = "cemaldak"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def login_with_token(self):
        data = {
            "username": "cemaldak",
            "password": "cemaldak"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_is_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_with_valid_information(self):
        self.login_with_token()
        data = {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "profile": {
                "id": 1,
                "note": "qwdqwd",
                "twitter": "qwdqwdqwd"
            }
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content),data)

    def test_with_empty_information(self):
        self.login_with_token()
        data = {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "profile": {
                "id": 1,
                "note": "",
                "twitter": ""
            }
        }
        response = self.client.put(self.url, data,format='json')
        self.assertEqual(200, response.status_code)
