import React, { useEffect, useState } from 'react';
import './App.css';
import CityContainer from '../City/CityContainer'

// Away we go!
const App = () => {

  const [data, setData] = useState();

  // Fetch data from the server
  const fetchData = async () => {
    let success = false;
    await fetch('data')
    .then((res)=> res.json())
    .then(res => {
      if (res.data) {
        setData(res.data);
        success = true;
      }
    })
    .catch(error => console.log(error));
    if (!success) setData([]);
  };

  // Fetch data from the server every 5 seconds
  useEffect(() => {
    const timer = setInterval(fetchData, 5000);
    return () => clearInterval(timer);
  }, [])

  const time = new Date().toLocaleTimeString();

  // Away we go!
  return (

    <div className="App">
      {!data ? (
        <div className="App--No-Data">Loading...</div>
      ) : (
        data && data.length ? (
          data.map((place, i) => <CityContainer key={i} data={place} updatedTime={time}/>)
        ) : (
          <div className="App--No-Data">Unable to fetch data from the server</div>
        )
      )}    
    </div>

  );
};

export default App;
