# Hello Celery

A Celery hello world project

## To run the backend

`docker compose up -d`

## Run proj

`celery -A proj worker -c 4 -l INFO`

## Run main 

```shell
celery -A tasks worker -c 16 -l INFO
python main.py
```