from celery import Celery
import time

app = Celery('tasks', backend='rpc://', broker='amqp://guest:guest@localhost//')

@app.task
def add(x, y):
    time.sleep(3)
    return x + y