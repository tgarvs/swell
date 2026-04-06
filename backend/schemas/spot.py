
from pydantic import BaseModel
from typing import List

class Spot (BaseModel) :
    id: str
    name: str
    latitude: float
    longitude: float


class HourlyReading(BaseModel):
    time : str
    wave_height: float
    wave_period: float
    wave_direction: float
    wind_speed: float
    wind_direction: float


class ForecastResponse(BaseModel):
    spot_id: str
    spot_name: str
    readings: List[HourlyReading]
