import React from 'react';
import './App.css';
import CityContainer from '../City/CityContainer'

const bridgewater = {
  city: 'Bridgewater',
  state: 'New Jersey',
  zipcode: '08807',
  temp: 36,
  message: 'dweeb'
};

const sanFrancisco = {
  city: 'San Francisco',
  state: 'California',
  zipcode: '94103',
  temp: 55
};

// Away we go!
const App = () => {

  return (

    <div className="App">
      <CityContainer data={bridgewater}/>
      <CityContainer data={sanFrancisco}/>
    </div>

  );
};

export default App;
