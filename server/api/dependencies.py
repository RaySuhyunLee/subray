from repositories.train_repository import InMemoryTrainRepository
from services.train_service import TrainService


def get_train_service() -> TrainService:
    return TrainService(train_repo=InMemoryTrainRepository())
