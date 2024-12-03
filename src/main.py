from celery.schedules import crontab

from tasks import *


app.conf.update(
    CELERYBEAT_SCHEDULE={
        "crontab_func1": {
            'task': 'tasks.crontab_func1',
            'schedule': crontab(minute='*/5'),
            'args': ()
        },
        "crontab_func2": {
            'task': 'tasks.crontab_func2',
            'schedule': crontab(minute='*/5'),
            'args': ()
        },
    },
)
