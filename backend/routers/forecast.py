from services.forecast import process_forecast
from services.stormglass import get_stormglass
from fastapi import APIRouter
import routers.utils as utils


spot_list = utils.get_spot_list()

router = APIRouter(
    prefix = "",
    responses={404: {"description": "Not found"}}
)

@router.get("/forecast/{spot_id}")
def get_forecast(spot_id: str):
    spot = utils.does_spot_exist(spot_list, spot_id)
    spot_data = get_stormglass(spot.latitude, spot.longitude)
    return process_forecast(spot_data, spot)