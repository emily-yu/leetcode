import React from "react"
import { useState, useRef, useEffect } from "react"

export function usePrevious<T>(value: T): T | undefined {
  // your code here

  // const [previous, setPrevious] = useState(value)
  // const val = useRef(undefined)
  // useEffect(() => {
  //   val.current = value
  //   return val
  // })
  // return value

  // notes
  // stores empty TYPED value t, since return value is typed fName<T>
  const refValue = useRef<T>()

  // track previous value for return, then set .current value to store
  const previousValue = refValue.current
  refValue.current = value
  return previousValue
}

// if you want to try your code on the right panel
// remember to export App() component like below

export function App() {

  // testing it wrong
  /*
  usePrevious('firstValue') // return firstValue
  usePrevious('secondValue') // return firstValue
  usePrevious('thirdValue') // return secondValue
  console.log(one, two, three)
  return <div>your app</div>
  */

  /* notes after reading solutions / how to test
      - seems i did not fully understand what a hook was
      - used to modify a state value 
  */
  const [counter, setCounter]= useState(0);
  const preveiousValue = usePrevious(counter);
  return (
    <>
    <p>previous value {preveiousValue} </p>
    <p>current value {counter}</p>
    <button onClick={() => setCounter(counter+1)}>+</button>
    </>
  )
}


