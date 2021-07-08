from kombu.utils.url import safequote
from celery import Celery
import os

def make_celery() -> Celery:

    aws_access_key = safequote(os.environ['AWS_USER_ID'])
    aws_secret_key = safequote(os.environ['AWS_USER_KEY'])

    broker_url = f"sqs://{aws_access_key}:{aws_secret_key}@"
    broker_transport_options = {'region': os.environ['AWS_REGION']}
    
    celery = Celery('tasks', broker=broker_url)
    celery.conf.update(
        broker_transport_options=broker_transport_options
    )

    return celery


celery: Celery = make_celery()