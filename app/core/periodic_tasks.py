from django_celery_beat.models import CrontabSchedule, IntervalSchedule

CELERY_BEAT_SCHEDULE = {
    "delete_outdated_cart_at_midnight": {
        "task": "store.tasks.delete_outdated_cart",
        # update every day at midnight
        "schedule": CrontabSchedule(minute='0', hour='0'),
    },
    #* This is just for testing purposes to see the task is working properly *#
    # "delete_outdated_cart_every_10_s": {
    #     "task": "store.tasks.delete_outdated_cart",
    #     "schedule": IntervalSchedule.objects.create(every=10, period=IntervalSchedule.SECONDS),
    # },
}