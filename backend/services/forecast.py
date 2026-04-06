import schemas.spot as ss


def process_forecast(raw_data, spot):
    hourlyforecasts = []
    for d in raw_data['hours']:
        t = d['time']
        waveDirection = d['waveDirection'].get('sg', 0.0)
        waveHeight = d['waveHeight'].get('sg', 0.0)
        wavePeriod = d['wavePeriod'].get('sg', 0.0)
        windDirection = d['windDirection'].get('sg', 0.0)
        windSpeed = d['windSpeed'].get('sg', 0.0)

        hourlyforecasts.append(ss.HourlyReading(time=t,
                                                wave_height=waveHeight,
                                                wave_period=wavePeriod,
                                                wave_direction=waveDirection,
                                                wind_speed=windSpeed,
                                                wind_direction=windDirection))
        
    return ss.ForecastResponse(spot_id=spot.id, spot_name=spot.name, readings=hourlyforecasts)
