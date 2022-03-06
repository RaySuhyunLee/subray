from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel


class SubwayDirection(Enum):
    UP_OR_OUTER_CIRCLE = 0
    DOWN_OR_INNER_CIRCLE = 1


class SeoulSubwayLocationPayload(BaseModel):
    subwayId: str
    subwayNm: str  # readable line name (ex. 2호선)
    statnId: str  # station Id
    statnNm: str  # station name
    trainNo: str
    lastRecptnDt: date  # last update date
    recptnDt: datetime  # last update time
    updnLine: SubwayDirection
    statnTid: str  # last station id
    statnTnm: str  # last station name
    directAt: int  # 0: normal, 1: express
    lstcarAt: int  # 0: normal, 1: last train

    @property
    def is_express(self) -> bool:
        return self.directAt == 1

    @property
    def is_last_train(self) -> bool:
        return self.lstcarAt == 1
