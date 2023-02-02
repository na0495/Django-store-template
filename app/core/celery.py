import os

from celery import Celery
from core import celery_config

# -------------------------------------------------

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

celery_app = Celery('core')
celery_app.config_from_object(celery_config)
celery_app.autodiscover_tasks()
