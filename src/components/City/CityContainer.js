import React from 'react';
import './CityContainer.css';

const red = [45, 51, 90, 119, 128, 165, 233, 233, 176, 116];
const green = [16, 64, 144, 197, 206, 204, 199, 102, 62, 27];
const blue = [87, 160, 230, 230, 210, 144, 95, 54, 33, 17];

const bColor = (temp) => {
    
    let topIndex = Math.floor(temp / 10);
    
    if (topIndex < 1) {
        topIndex = 1;
    } else if (topIndex > 9) {
        topIndex = 9;
    }

    return {
        cityContainer: `linear-gradient(rgb(${red[topIndex]}, ${green[topIndex]}, ${blue[topIndex]}), rgb(${red[topIndex-1]}, ${green[topIndex-1]}, ${blue[topIndex-1]}))`,
        weeksContainer: `rgba(${red[topIndex]}, ${green[topIndex]}, ${blue[topIndex]}, 0.3)`
    };
};

const CityContainer = ({data, updatedTime}) => {

    return (
        <div className="CityContainer" style={{background: bColor(data.temp).cityContainer}}>
            <div className="CityContainer-City" >{data.name}</div>
            <div className="CityContainer-Temp" >{data.temp}&deg;</div>
            <div className="CityContainer-Message" > {data.phrase}</div>
            <div className="CityContainer-Time">{`Updated At: ${updatedTime}`}</div>
        </div>
    );
};

export default CityContainer;
