from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SeoulSubwayTrainStatus(Enum):
    ARRIVING = 0
    ARRIVED = 1
    DEPARTED = 2


class SeoulSubwayArrivalPayload(BaseModel):
    subwayNm: str  # readable line name (ex. 2호선)
    statnId: str  # station Id
    statnNm: str  # station name
    trainNo: str
    recptnDt: datetime  # last update time
    trainSttus: SeoulSubwayTrainStatus

    class Config:
        extra = 'ignore'
