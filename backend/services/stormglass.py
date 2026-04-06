from dotenv import load_dotenv
from datetime import datetime, timedelta
import httpx
import os

load_dotenv()
def get_stormglass(lat: float, lng: float):
    
    start = datetime.now(datetime.timezone.utc)
    end = start + timedelta(hours=24)   

    response = httpx.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': lat,
        'lng': lng,
        'params': ','.join(['waveHeight', 
                            'wavePeriod',
                            'waveDirection',
                            'windDirection',
                            'windSpeed',
                            ]),
        'start': start.timestamp(),
        'end': end.timestamp()
    },
    headers={
        'Authorization': os.getenv("STORMGLASS_API_KEY")
    }
    )

    return response.json()