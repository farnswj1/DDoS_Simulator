from rest_framework.generics import ListCreateAPIView
from core.serializers import DataSerializer
from core.filters import DataFilterSet
from core.models import Data

# Create your views here.
class DataListCreateAPIView(ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filterset_class = DataFilterSet
