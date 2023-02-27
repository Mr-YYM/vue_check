import ipaddress

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import Port
from .serializers import PortSerializer

class PortViewSet(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

    def create(self, request, *args, **kwargs):
        # 获取请求中的IP地址和端口号
        ip_address = request.data.get('ip_address')
        port = request.data.get('port_number')

        # 检查IP地址和端口号的格式是否正确
        if not self.validate_ip_address(ip_address) or not self.validate_port(port):
            return Response(
                {'error': 'Invalid IP address or port number.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 将请求数据转换为Port对象，并保存到数据库
        serializer = PortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        # 获取请求中的IP地址和端口号
        ip_address = request.data.get('ip_address')
        port = request.data.get('port')

        # 检查IP地址和端口号的格式是否正确
        if not self.validate_ip_address(ip_address) or not self.validate_port(port):
            return Response(
                {'error': 'Invalid IP address or port number.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 根据URL中的ID获取要更新的Port对象
        instance = self.get_object()

        # 将请求数据更新到Port对象中，并保存到数据库
        serializer = PortSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate_ip_address(self, ip):
        try:
            # 尝试将IP地址解析为IPv4或IPv6对象
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    def validate_port(self, port):
        try:
            # 将端口号转换为int类型，并确保它在0到65535之间
            port_num = int(port)
            return 0 <= port_num <= 65535
        except ValueError:
            return False
