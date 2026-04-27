import { useEffect } from "react";
import { useState } from 'react'



function SpotSelector ({onSpotSelect}){
    const[spotList, setSpots] = useState([]) //need brackets bc we are going to pass in a list, this creates a state and state set 

    // this runs once when the component loads bc of the ending []
    useEffect(() => {
        fetch('http://localhost:8000/spots')
        .then(res => res.json())
        .then(data => {
            console.log(data)
            setSpots(data)
        })
    }, [])


  return (
    <div> 
      {spotList.map(spot => ( //iterate over spotlist using map
        <button onClick={() => onSpotSelect(spot.id)}
                key={spot.id}
                className="m-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
        >{spot.name} </button>      ))}
    </div>
  )
}


export default SpotSelector 
