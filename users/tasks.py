from celery import shared_task
import time

@shared_task
def multiply_by_ten(number):
    num = number * 10
    time.sleep(5)
    return num