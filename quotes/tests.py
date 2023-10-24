from django.test import TestCase
from .models import Quote


class QuoteTestCase(TestCase):
    def setUp(self):
        Quote.objects.create(
            name="John Doe", email="john@example.com", message="Hello World"
        )

    def test_quote_content(self):
        quote = Quote.objects.get(name="John Doe")
        self.assertEqual(quote.email, "john@example.com")
        self.assertEqual(quote.message, "Hello World")
