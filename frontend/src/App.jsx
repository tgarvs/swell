import { useState, useEffect } from 'react'
import SpotSelector from './components/SpotSelector'

function App() {
  const[selectedSpot, setSelectedSpot] = useState(null)
  const[forecasts, setForecast] = useState(null)

    useEffect(() => {
        if(selectedSpot == null) return
        fetch('http://localhost:8000/forecast/' + selectedSpot)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            setForecast(data)
        })
    }, [selectedSpot])

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold">Swell</h1>
      <SpotSelector onSpotSelect={setSelectedSpot}/>
      <p className="text-1xl">{selectedSpot}</p>
      {forecasts && forecasts.readings.map(reading => 
        <div key={reading.time}>
          <p className="text-1xl font-italics">Wind Time: {reading.time}</p>
          <p className="text-1xl font-italics">Wind Speed: {reading.wind_speed}</p>
          <p className="text-1xl font-italics">Wind Direction: {reading.wind_direction}</p>
          <p className="text-1xl font-italics">Wave Direction: {reading.wave_direction}</p>
          <p className="text-1xl font-italics">Wave Period: {reading.wave_period}</p>
          <p className="text-1xl font-italics">Wave Height: {reading.wave_height}</p>
        </div>
      )}

    </div>
  )
}

export default App