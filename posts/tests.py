from django.test import TestCase
from .models import Category, Post


class PostTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Tech", description="Technology")
        post = Post.objects.create(title="New Gadget", content="Awesome content here")
        post.categories.add(category)

    def test_post_title(self):
        post = Post.objects.get(title="New Gadget")
        self.assertEqual(post.content, "Awesome content here")

    def test_category_name(self):
        category = Category.objects.get(name="Tech")
        self.assertEqual(category.description, "Technology")
