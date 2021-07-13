from tasks import add
from celery import group
import logging

logging.basicConfig(
	format='%(asctime)s %(levelname)-8s %(message)s',
	level=logging.INFO,
	datefmt='%Y-%m-%d %H:%M:%S')

logging.info("Start")

n = 1000;


g = group(add.s(i) for i in range(n))
result = g(1).get()

logging.info("End %s" % len(result))