from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PortfolioViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"portfolios", PortfolioViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
