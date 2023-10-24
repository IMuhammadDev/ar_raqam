from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("core/", include("core.urls")),
    path("projects/", include("projects.urls")),
    path("posts/", include("posts.urls")),
    path("portfolios/", include("portfolios.urls")),
    path("quotes/", include("quotes.urls")),
    path("services/", include("services.urls")),
    path("common/", include("common.urls")),
    path("industries/", include("industries.urls")),
    path("accounts/", include("allauth.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    # Add other apps as needed
]
