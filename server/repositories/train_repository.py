from abc import ABC, abstractmethod
from typing import List

from schemas.train import Train


class TrainRepositoryBase(ABC):
    @abstractmethod
    async def get_trains(self) -> List[Train]:
        raise NotImplementedError()
