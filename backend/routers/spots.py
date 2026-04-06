

import json
from schemas.spot import Spot
from fastapi import APIRouter, HTTPException


with open("backend/data/spots.json") as f :
    data = json.load(f)
spot_list = [Spot(**spot_dict) for spot_dict in data]

router = APIRouter(
    prefix = "",
    responses={404: {"description": "Not found"}}
)

@router.get("/spots")
def get_spots() :
    return spot_list


@router.get("/spots/{spot_id}") 
def get_specific_spot(spot_id: str) :
    for spot in spot_list :
        if spot_id == spot.id :
            return spot

    raise HTTPException(status_code=404, detail="Spot not found") 
    

