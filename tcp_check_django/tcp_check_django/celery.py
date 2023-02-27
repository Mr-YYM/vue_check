# celery.py

import os
from celery import Celery

# 设置 Celery 的默认配置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tcp_check_django.settings')
app = Celery('tcp_check_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
