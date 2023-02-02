import os
from .celery import celery_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
__all__ = ['celery_app']
