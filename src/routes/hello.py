from fastapi import APIRouter
from src.services.hello_queue_service import HelloQueueService
from src.models.hello import HelloModel, HelloResponseModel

router  = APIRouter(
    prefix='/hello',
    tags=['hello'],
    responses={404: {'description': 'Not found'}},
)


@router.post("/", response_model=HelloResponseModel)
def hello(model: HelloModel):
    service = HelloQueueService()
    return service.queue(model)