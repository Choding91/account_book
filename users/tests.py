from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User


class UserTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user("test@test.com", "1234")
        cls.data = {"email": "test@test.com", "password": "1234"}

    def setUp(self):
        self.access_token = self.client.post(reverse("token_obtain_pair"), self.data).data["access"]
        self.refresh_token = self.client.post(reverse("token_obtain_pair"), self.data).data["refresh"]

    def test_register(self):
        response = self.client.post(
            path=reverse("signup_view"),
            data={"email": "email@email.com", "password": "1234"},
        )
        self.assertEqual(response.status_code, 201)

    def test_unregister(self):
        response = self.client.delete(
            path=reverse("signup_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 204)

    def test_login(self):
        response = self.client.post(
            path=reverse("token_obtain_pair"),
            data=self.data,
        )
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.post(
            path=reverse("token_blacklist"),
            data={"refresh": self.refresh_token},
        )
        self.assertEqual(response.status_code, 200)
