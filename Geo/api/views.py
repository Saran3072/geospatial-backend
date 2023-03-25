from rest_framework import viewsets
from ..models import geo
from .serializers import GeoSerializer

class imageViewSet(viewsets.ModelViewSet):
    serializer_class = GeoSerializer
    queryset = geo.objects.all()
    