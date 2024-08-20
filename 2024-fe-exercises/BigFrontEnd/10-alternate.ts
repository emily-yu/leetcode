// https://bigfrontend.dev/react/phone-number-input
// formats while typing instead of after typing

import React, { useState } from 'react'
export function PhoneNumberInput() {
  // your code here

  const [number, setNumber] = useState()

  // only numerical + format inputs
  const checkData = () => {
    let input = document.getElementsByTagName('input')[0]
    // console.log(input.value)

    // console.log(input.value.slice(-1))
    const test = Number(input.value.slice(-1))
    // console.log(test)
    if (isNaN(test)) {
      const beep = input.value.slice(0, -1)
      // console.log('beep', beep)
      input.value = beep
      throw Error("not an int")
      return
    }
    else {
      // format value shown
      if (input.value.length == 1) input.value = "(" + input.value
      if (input.value.length == 4) input.value = input.value + ")"
      if (input.value.length == 8) input.value = input.value + "-"
    }
  }

  return <input 
            onChange={checkData} 
            data-testid="phone-number-input"/>
}

// if you want to try your code on the right panel
// remember to export App() component like below

export function App() {
  return <PhoneNumberInput/>
}








