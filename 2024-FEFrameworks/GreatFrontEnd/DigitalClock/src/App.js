import React from 'react';

export function App(props) {
  return (
    <div className='App'>
      <Clock/>
    </div>
  );
}

import moment from 'moment';
import { useState, useEffect } from 'react'
export default function Clock() {

  const [time, setTime] = useState(Date.now())

  const getTimeLabel = () => {
    var d = new Date();
    var formatteddatestr = moment(d).format('hh:mm:ss');
    return formatteddatestr
  }

  useEffect(() => {
    setTime(getTimeLabel())
    setInterval(function() {
      // console.log("Message to alert every 5 seconds");
      setTime(getTimeLabel())
    }, 1000);
  })

  return <div>{time}</div>;
}

// Log to console
console.log('Hello console')