from src.models.hello import HelloModel, HelloResponseModel
from datetime import datetime, time
from src.services.hello_service import HelloService
from src.tasks.hello_tasks import send_message

class HelloQueueService:
    def queue(self, model: HelloModel) -> HelloResponseModel:
        send_message.delay(model.name, model.message)
        # HelloService().send_hello(model)
        return HelloResponseModel(status='queued', time=datetime.now())
