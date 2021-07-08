from celeryapp import celery
from src.models.hello import HelloModel
from src.services.hello_service import HelloService

@celery.task(name="send_message")
def send_message(name, message):
    model = HelloModel(name=name, message=message)
    HelloService().send_hello(model)
