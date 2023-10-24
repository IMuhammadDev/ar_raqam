from .models import Industry
from .serializers import IndustrySerializer
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
