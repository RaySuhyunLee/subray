from api.dependencies import get_train_service
from fastapi import APIRouter, Depends
from schemas.train import TrainPayload
from services.train_service import TrainService

router = APIRouter()


@router.get('/subway/locations')
async def get_subway_locations(
    train_service: TrainService = Depends(get_train_service)
) -> TrainPayload:
    trains = await train_service.get_all_trains()
    return TrainPayload(trains=trains)
