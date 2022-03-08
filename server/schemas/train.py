from enum import Enum
from typing import List

from pydantic import BaseModel


class SubwayLocation(BaseModel):
    departure_station_id: str
    arrival_station_id: str
    normalized_location: float  # location between two stations [0~1]


class TrainStatus(str, Enum):
    STOPPED = "STOPPED"
    MOVING = "MOVING"


class Train(BaseModel):
    line_number: int
    train_id: str
    location: SubwayLocation
    status: TrainStatus


class TrainPayload(BaseModel):
    trains: List[Train]
