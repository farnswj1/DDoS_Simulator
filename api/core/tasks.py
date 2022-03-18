from celery import shared_task
from core.models import Data


@shared_task(name='core.delete_data')
def delete_data():
    Data.objects.all().delete()
