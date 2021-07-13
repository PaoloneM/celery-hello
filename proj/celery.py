from celery import Celery

app = Celery(	'proj', 
		backend='redis://localhost', 
		broker='amqp://guest:guest@localhost//',
        	include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
