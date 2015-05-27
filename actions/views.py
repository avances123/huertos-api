from rest_framework import viewsets
from actstream.models import model_stream
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from actions.serializers import ActionSerializer
from farms.models import Farm


class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset           = model_stream(Farm)
    serializer_class   = ActionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)