import { useEffect } from "react";
import { useState } from 'react'



function SpotSelector (){
    const[spotList, setSpots] = useState([]) //need brackets bc we are going to pass in a list

    useEffect(() => {
        fetch('http://localhost:8000/spots')
        .then(res => res.json())
        .then(data => {
            console.log(data)
            setSpots(data)
        })
    }, [])

  return ( //what does <div> do?
    <div> 
      {spotList.map(spot => ( //iterate over spotlist using map
        <button 
        key={spot.id}
        className="m-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
        >
        {spot.name}
        </button>      ))}
    </div>
  )
}


export default SpotSelector //what does this do?
