from abc import ABC, abstractmethod
from typing import Dict, List

from schemas.train import Train


class TrainRepositoryBase(ABC):
    @abstractmethod
    async def get_trains(self) -> List[Train]:
        raise NotImplementedError()

    @abstractmethod
    async def set_trains(self, trains: List[Train]) -> None:
        raise NotImplementedError


class InMemoryTrainRepository(TrainRepositoryBase):
    def __init__(self):
        super().__init__()
        self.trains: Dict[str, Train] = {}

    async def get_trains(self) -> List[Train]:
        return [v for _, v in self.trains.items()]

    async def set_trains(self, trains: List[Train]) -> None:
        for train in trains:
            self.trains[train.train_id] = train
