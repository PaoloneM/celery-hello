from tasks import add
import logging

logging.basicConfig(
	format='%(asctime)s %(levelname)-8s %(message)s',
	level=logging.INFO,
	datefmt='%Y-%m-%d %H:%M:%S')

logging.info("Start")

result = add.delay(4,4)

state = ""
while state != "SUCCESS":
	nextState = result.status
	if (state != nextState):
		state = nextState
		logging.info(state)

logging.info("End %s" % result.get())
result.forget()