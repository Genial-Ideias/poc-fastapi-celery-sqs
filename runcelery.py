from celery.app.base import Celery
from celery import Celery
from src.tasks import hello_tasks
from celeryapp import celery

app: Celery = celery