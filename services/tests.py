from django.test import TestCase
from .models import Service, Category


class ServiceTestCase(TestCase):
    def setUp(self):
        Service.objects.create(
            description="Service 1", price="100.00", duration="01:00:00"
        )
        Service.objects.create(
            description="Service 2", price="200.00", duration="02:00:00"
        )

    def test_service_description(self):
        service1 = Service.objects.get(price="100.00")
        service2 = Service.objects.get(price="200.00")
        self.assertEqual(service1.description, "Service 1")
        self.assertEqual(service2.description, "Service 2")


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Category 1", description="Description 1")
        Category.objects.create(name="Category 2", description="Description 2")

    def test_category_name(self):
        category1 = Category.objects.get(name="Category 1")
        category2 = Category.objects.get(name="Category 2")
        self.assertEqual(category1.description, "Description 1")
        self.assertEqual(category2.description, "Description 2")
