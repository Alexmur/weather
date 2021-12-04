import React from 'react';
import './App.css';
import CityContainer from '../City/CityContainer'

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
