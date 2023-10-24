from rest_framework import serializers
from .models import Category, Portfolio


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = "__all__"
