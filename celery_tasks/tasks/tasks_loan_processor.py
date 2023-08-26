import time
from celery import shared_task

@shared_task(queue='default')
def slow_task():
    print('Started task, processing...')
    time.sleep(5)
    print('Finished Task')
    return True

slow_task.delay()