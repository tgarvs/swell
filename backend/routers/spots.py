
import routers.utils as utils
from fastapi import APIRouter

spot_list = utils.get_spot_list()

router = APIRouter(
    prefix = "",
    responses={404: {"description": "Not found"}}
)

@router.get("/spots")
def get_spots() :
    return spot_list


@router.get("/spots/{spot_id}") 
def get_specific_spot(spot_id: str) :
    utils.does_spot_exist(spot_list, spot_id)
    


