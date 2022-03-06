from enum import Enum

from pydantic import BaseModel


class SubwayLocation(BaseModel):
    departure_station_id: str
    arrival_station_id: str
    normalized_location: float  # location between two stations [0~1]


class SubwayStatus(str, Enum):
    STOPPED = "STOPPED"
    MOVING = "MOVING"


class Subway(BaseModel):
    line_number: int
    train_number: str
    location: SubwayLocation
    status: SubwayStatus
