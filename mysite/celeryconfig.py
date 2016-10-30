from kombu import Exchange, Queue
from datetime import timedelta
BROKER_URL = 'amqp://'


CELERYBEAT_SCHEDULE = {
    'posting': {
        'task': 'glue.tasks.post_things',
        'schedule': timedelta(seconds=15),
    },
}
CELERY_ALWAYS_EAGER = False
CELERY_DEFAULT_QUEUE = 'app1'
CELERY_QUEUES = (
    Queue('app1', Exchange('app1'), routing_key='app1'),
)
