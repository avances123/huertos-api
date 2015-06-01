from rest_framework import viewsets
from farms.models import Farm,Zone
from farms.serializers import FarmSerializer,ZoneSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import detail_route
from actstream import action
from rest_framework.response import Response
from rest_framework import status
from farms.permissions import IsOwnerOrReadOnly






class FarmViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset           = Farm.objects.all()
    serializer_class   = FarmSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    @detail_route(methods=['post'])
    def regar(self, request, pk=None):
        instance = self.get_object()
        action.send(instance.owner, verb='regar',action_object=instance,color="#348923")
        return Response(None,status=status.HTTP_204_NO_CONTENT)





class ZoneViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
