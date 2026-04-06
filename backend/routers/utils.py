import json
from schemas.spot import Spot
from fastapi import HTTPException


def get_spot_list() :
    with open("data/spots.json") as f :
        data = json.load(f)
    spot_list = [Spot(**spot_dict) for spot_dict in data]
    return spot_list


def does_spot_exist(spot_list, spot_id):
    for spot in spot_list :
        if spot_id == spot.id :
            return spot
    raise HTTPException(status_code=404, detail="Spot not found") 