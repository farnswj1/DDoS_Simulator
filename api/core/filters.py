from django_filters.rest_framework import FilterSet, CharFilter
from core.models import Data

class DataFilterSet(FilterSet):
    username = CharFilter('username', label='Username', lookup_expr='icontains')

    class Meta:
        model = Data
        fields = ('username',)
