# <>/tasks.py
from celery import shared_task
import time
@shared_task
def do_something(x, y):
    time.sleep(1)
    return x + y

@shared_task
def do_multi(x, y):
    time.sleep(1)
    return x * y