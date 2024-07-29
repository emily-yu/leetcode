/*
  notes (1/2 test cases)
    - did okay in general
    - pieced apart problem fine while looking at prior code
    - wrote out tests fine and tested it with understanding problem
    - didn't implement full useEffect functionality (cleanup, see below)
*/

import React, { useEffect, useState } from 'react'
import { EffectCallback, useRef } from 'react'

export function useEffectOnce(effect: EffectCallback) {
  // your code here

  const hasRan = useRef<boolean>(false)

  useEffect(() => {
    if (hasRan.current == false) {
      hasRan.current = true

      // my error: didn't return the effect to prevent from 
      return effect()
    }
  }, [])
}

// if you want to try your code on the right panel
// remember to export App() component like below

export function App() {
  const testEffect = () => {
    return 'idiot'
  }

  const [value, setValue] = useState('0')
  useEffect(() => {
    setValue(testEffect)
    setValue(testEffect)
  })
  return (
    <>
      <div>{value}</div>
    </>
  )
}



