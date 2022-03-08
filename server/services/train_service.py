from typing import List

from repositories.train_repository import TrainRepositoryBase
from schemas.train import Train


class TrainService():
    def __init__(self, train_repo: TrainRepositoryBase):
        self.train_repo = train_repo

    async def get_all_trains(self) -> List[Train]:
        trains = await self.train_repo.get_trains()
        return trains
