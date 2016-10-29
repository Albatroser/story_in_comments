from datetime import timedelta
BROKER_URL = 'amqp://'


CELERYBEAT_SCHEDULE = {
    'posting': {
        'task': 'glue.tasks.post_things',
        'schedule': timedelta(seconds=5),
    },
}
CELERY_ALWAYS_EAGER = False
