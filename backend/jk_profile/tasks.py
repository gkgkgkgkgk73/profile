# <>/tasks.py
from celery import shared_task
import time
@shared_task
def do_something(x, y):
    return x + y

@shared_task
def do_multi(x, y):
    return x * y