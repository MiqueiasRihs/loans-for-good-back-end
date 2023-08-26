import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loans_for_good.settings') #1
app = Celery('celery_tasks', broker=settings.CELERY_BROKER_URL) #2
app.config_from_object('django.conf:settings', namespace='CELERY') #3
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #4
