from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.utils import json
from post.models import Post
from favourite.models import Favourite

class FavouriteCreateList(APITestCase):
    url = reverse("favourite:list-create")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "cemaldak"
        self.password = "cemaldak"
        self.user = User.objects.create_user(username=self.username,password=self.password)
        self.post = Post.objects.create(user = self.user,title="başlık", content="içerik")
        self.test_jwt_authentication()

    def test_jwt_authentication(self):
        response = self.client.post(self.url_login,data = {"username":self.username,"password":self.password})
        self.assertEqual(200,response.status_code)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_add_favourite(self):
        data = {
            "content": "içerik güzel favla",
            "user": self.user.id,
            "post": self.post.id,
        }
        response = self.client.post(self.url,data)
        self.assertEqual(201,response.status_code)

    def test_user_favs(self):
        self.test_add_favourite()
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)["results"]) == Favourite.objects.filter(user = self.user).count())

