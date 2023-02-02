import datetime

import pytz
from celery import shared_task

from .models import Cart

# ---------------
# store tasks ---
# ---------------

utc = pytz.UTC


@shared_task
def delete_outdated_cart():
    """
    Delete carts that are older than 60 days
    """
    outdated = utc.localize(datetime.datetime.now() - datetime.timedelta(days=60))
    # get all carts that are older than 60 days
    carts = Cart.objects.filter(created_at__lt=outdated)
    count = carts.count()
    carts.delete()
    return {
        'status': 'success',
        'message': f'Outdated carts are deleted, ({count} carts deleted)',
    }
