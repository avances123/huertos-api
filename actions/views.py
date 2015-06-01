from rest_framework import generics
from actstream.models import model_stream
from actions.serializers import ActionSerializer
from farms.models import Farm



class AllFarmActions(generics.ListAPIView):
    queryset = model_stream(Farm)
    serializer_class   = ActionSerializer



