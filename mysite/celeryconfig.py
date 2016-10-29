from datetime import timedelta
BROKER_URL = 'amqp://'


CELERYBEAT_SCHEDULE = {
    'post_stories_if_it_posted': {
        'task': 'glue.tasks.post_story',
        'schedule': timedelta(seconds=15),
    }
}
CELERY_ALWAYS_EAGER = False
