from tasks import add
from celery import group
import logging

logging.basicConfig(
	format='%(asctime)s %(levelname)-8s %(message)s',
	level=logging.INFO,
	datefmt='%Y-%m-%d %H:%M:%S')

logging.info("Start")

n = 50000;
result = []

for i in range(n):
	result.append(add.delay(1, i))

logging.info("All task started")

for i in range(n):

	logging.info("Waiting for result #%s" % i)
	res = result[i].get()
	if res != i + 1:
		logging.error("Error: result #%s" % i)
	else:
		logging.info("Got result: %s" % res)

logging.info("End %s" % result[n-1].get())