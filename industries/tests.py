from django.test import TestCase
from .models import Industry


class IndustryTestCase(TestCase):
    def setUp(self):
        Industry.objects.create(name="Industry 1", description="Description 1")
        Industry.objects.create(name="Industry 2", description="Description 2")

    def test_industry_name(self):
        industry1 = Industry.objects.get(name="Industry 1")
        industry2 = Industry.objects.get(name="Industry 2")
        self.assertEqual(industry1.description, "Description 1")
        self.assertEqual(industry2.description, "Description 2")
