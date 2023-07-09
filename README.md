#  Tasks example

Simple implementation asynchronous tasks
(python, [Celery](https://docs.celeryq.dev/en/stable/), [RabbitMQ](https://www.rabbitmq.com/documentation.html), [Redis](https://redis.io/docs/))
  
based on https://github.com/vjanz/python-asynchronous-tasks

##  Setup & Installation 

Create a virtual environment and install the dependencies:
```bash
$ python -m venv venv
$ source env/bin/activate

$ pip install -r requirements.txt
```

Start Redis and RabbitMQ with docker-compose:

```bash
docker-compose up -d
```

Verify that the services are up and running:
```
$ docker ps
```

## Usage

Start the celery worker
```bash
$ celery -A tasks worker -l info --pool=solo
```

Start app.py
```bash
$ python app.py
```

## Note

Stop lifted containers:
```bash
$ docker-compose stop
```

Start stopped containers:
```bash
$ docker-compose start
```

Stop and delete containers and network:
```bash
$ docker-compose down
```

Remove Redis image:
```bash
$ docker rmi redis
```

Remove RabbitMQ image:
```bash
$ docker rmi rabbitmq