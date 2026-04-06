
from pydantic import BaseModel

class Spot (BaseModel) :
    id: str
    name: str
    latitude: float
    longitude: float