from rest_framework import viewsets

from .models import Confession
from .serializers import ConfessionSerializer


class ConfessionViewSet(viewsets.ModelViewSet):
    queryset = Confession.objects.all().order_by('-id')
    serializer_class = ConfessionSerializer
    http_method_names = ["get", "post", "head"]
