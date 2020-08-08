
from rest_framework import serializers


class WorkerSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_available = serializers.BooleanField()
    primary_phone = serializers.CharField()
    secondary_phone = serializers.CharField()
    address = serializers.CharField()
