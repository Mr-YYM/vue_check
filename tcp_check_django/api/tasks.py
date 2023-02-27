from celery import shared_task
import socket
from .models import Port

@shared_task
def check_ports():
    for port in Port.objects.all():
        ip_address, port_number = port.ip_address, port.port_number
        try:
            sock = socket.create_connection((ip_address, port_number), timeout=1)
            sock.close()
            port.is_open = True
        except:
            port.is_open = False
        port.save()
