from rest_framework import serializers
from .models import Port

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('id', 'ip_address', 'port_number', 'is_open')
