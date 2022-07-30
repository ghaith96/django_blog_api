from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

class PostTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testuser",
            password="super_secret_pass",
            email="test@example.com",
        )

        self.post = Post.objects.create(
            author = self.user,
            title = "post title",
            body = "post body",
        )


    def test_post_model(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.title, "post title")
        self.assertEqual(self.post.body, "post body")
        self.assertEqual(str(self.post), "post title")
