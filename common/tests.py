from django.test import TestCase
from .models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Category 1", description="Description 1")
        Category.objects.create(name="Category 2", description="Description 2")

    def test_category_name(self):
        category1 = Category.objects.get(name="Category 1")
        category2 = Category.objects.get(name="Category 2")
        self.assertEqual(category1.description, "Description 1")
        self.assertEqual(category2.description, "Description 2")
