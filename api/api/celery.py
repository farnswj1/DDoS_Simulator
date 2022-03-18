from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'core.delete_data': {
        'task': 'core.delete_data',
        'schedule': crontab(minute=0, hour='*')
    }
}

app.autodiscover_tasks()
