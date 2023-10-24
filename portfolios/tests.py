from django.test import TestCase
from .models import Category, Portfolio


class PortfoliosTestCase(TestCase):
    def setUp(self):
        category1 = Category.objects.create(
            name="Category 1", description="Description 1"
        )
        portfolio = Portfolio.objects.create(
            title="Portfolio 1", description="Description", date_completed="2023-01-01"
        )
        portfolio.categories.add(category1)

    def test_portfolio_title(self):
        portfolio = Portfolio.objects.get(title="Portfolio 1")
        self.assertEqual(portfolio.description, "Description")

    def test_category_name(self):
        category = Category.objects.get(name="Category 1")
        self.assertEqual(category.description, "Description 1")
