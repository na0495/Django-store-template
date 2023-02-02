import json

from core.periodic_tasks import CELERY_BEAT_SCHEDULE
from django_celery_beat.models import (CrontabSchedule, IntervalSchedule,
                                       PeriodicTask)

# -------------------------------------------------

tasks = PeriodicTask.objects.all()
for task in tasks:
    task.delete()
interval_schedules = IntervalSchedule.objects.all()
for interval_schedule in interval_schedules:
    interval_schedule.delete()
crontab_schedules = CrontabSchedule.objects.all()
for crontab_schedule in crontab_schedules:
    crontab_schedule.delete()

# defining the new taks
for task in CELERY_BEAT_SCHEDULE.keys():
    print('adding the task {}'.format(task))
    settings = CELERY_BEAT_SCHEDULE[task]

    schedule = settings['schedule']

    if isinstance(schedule, IntervalSchedule):
        s, _ = IntervalSchedule.objects.get_or_create(
            every=schedule.every, period=schedule.period
        )

        PeriodicTask.objects.get_or_create(
            interval=s,
            name=task,
            task=settings['task'],
            args=json.dumps(settings.get('args')),
            kwargs=json.dumps(settings.get('kwargs')),
            expires=settings.get('expires'),
        )

    if isinstance(schedule, CrontabSchedule):
        s, _ = CrontabSchedule.objects.get_or_create(
            minute=schedule.minute,
            hour=schedule.hour,
            day_of_week=schedule.day_of_week,
            day_of_month=schedule.day_of_month,
            month_of_year=schedule.month_of_year,
            timezone=schedule.timezone,
        )

        PeriodicTask.objects.get_or_create(
            crontab=s,
            name=task,
            task=settings['task'],
            args=json.dumps(settings.get('args')),
            kwargs=json.dumps(settings.get('kwargs')),
            expires=settings.get('expires'),
        )
