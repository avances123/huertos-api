from rest_framework import viewsets
from farms.models import Farm,Zone
from farms.serializers import FarmSerializer,ZoneSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from farms.permissions import IsOwnerOrReadOnly
from farms.filters import FarmFilter
from rest_framework.decorators import action






class FarmViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing farms.
    """
    queryset           = Farm.objects.all()
    serializer_class   = FarmSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    filter_class       = FarmFilter


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    @action(methods=['post'], detail=True)
    def regar(self, request, pk=None):
        zone = self.get_object()
        try:
            date = request.data['date']
            zone.last_water = request.data['date']
            zone.save()
            return Response({'status': 'password set'})
        except:
            return Response({'status': 'not a date'},
                            status=status.HTTP_400_BAD_REQUEST)




