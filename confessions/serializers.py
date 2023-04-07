from rest_framework import serializers

from .models import Confession


class ConfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confession
        fields = "__all__"
