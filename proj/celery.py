from celery import Celery
import itertools
import random
from datetime import datetime


def random_failover_strategy(servers):
    it = list(servers)  # don't modify callers list
    random.shuffle(it)
    for i in itertools.cycle(it):
        yield i

BROKER_URL = [
    "amqp://guest:guest@localhost:5672//",
    "amqp://guest:guest@localhost:6672//",
    "amqp://guest:guest@localhost:7672//"
]
BROKER_FAILOVER_STRATEGY = random_failover_strategy

random.shuffle(BROKER_URL)

app = Celery(	'proj', 
		backend='redis://localhost', 
		broker=BROKER_URL,
		broker_failover_strategy=BROKER_FAILOVER_STRATEGY,
		task_default_queue="celery-%s" % datetime.now(),
        	include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
