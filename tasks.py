from celery import Celery

from celery_worker import celery_worker

broker_url = "amqp://localhost"
redis_url = "redis://localhost"
app = Celery('tasks', broker=broker_url, backend=redis_url)


@app.task
def task(data_processor_number: int, data: int):
    return celery_worker(data_processor_number, data)
