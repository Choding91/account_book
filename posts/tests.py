from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from posts.models import Post


class PostTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user("test@test.com", "1234")
        cls.post = Post.objects.create(user=cls.user, account=10000, content="content")
        cls.user_data = {"email": "test@test.com", "password": "1234"}
        cls.post_data = {"account": 10000, "content": "content"}

    def setUp(self):
        self.access_token = self.client.post(reverse("token_obtain_pair"), self.user_data).data["access"]
        self.refresh_token = self.client.post(reverse("token_obtain_pair"), self.user_data).data["refresh"]

    def test_get_post(self):
        response = self.client.get(
            path=reverse("post_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        response = self.client.post(
            path=reverse("post_view"),
            data=self.post_data,
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 201)


class PostDetailTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user("test@test.com", "1234")
        cls.post = Post.objects.create(user=cls.user, account=10000, content="content")
        cls.user_data = {"email": "test@test.com", "password": "1234"}
        cls.post_data = {"account": 10000, "content": "content"}

    def setUp(self):
        self.access_token = self.client.post(reverse("token_obtain_pair"), self.user_data).data["access"]
        self.refresh_token = self.client.post(reverse("token_obtain_pair"), self.user_data).data["refresh"]

    def test_get_post_detail(self):
        response = self.client.get(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 200)

    def test_duplicate_post_detail(self):
        response = self.client.post(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 201)

    def test_update_post_detail(self):
        response = self.client.put(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            data=self.post_data,
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 202)

    def test_delete_post_detail(self):
        response = self.client.delete(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 204)
