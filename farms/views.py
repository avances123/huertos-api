from rest_framework import viewsets
from farms.models import Farm,Zone
from farms.serializers import FarmSerializer,ZoneSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from farms.permissions import IsOwnerOrReadOnly
from farms.filters import FarmFilter






class FarmViewSet(viewsets.ModelViewSet):
    queryset           = Farm.objects.all()
    serializer_class   = FarmSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    filter_class       = FarmFilter


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

