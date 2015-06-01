import django_filters
from farms.models import Farm

class FarmFilter(django_filters.FilterSet):
    class Meta:
        model = Farm
        fields = ['owner__username']