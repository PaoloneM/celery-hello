from celery import Celery
import time

broker_url = [
    'amqp://guest:guest@localhost:5672//',
    'amqp://guest:guest@localhost:6672//',
    'amqp://guest:guest@localhost:7672//',
]

app = Celery('tasks', backend='redis://localhost', broker=broker_url)

@app.task
def add(x, y):
    time.sleep(1)
    return x + y