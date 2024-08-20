/*
  notes
    - nice did it without needing solutions
*/

import React from "react"
import { useEffect, useRef, useState } from "react"

export function useIsFirstRender(): boolean {
  // your code here

  const rendered = useRef(true)

  // return state of rendered
  if (rendered.current) {
    rendered.current = false
    return true
  }
  return false
}

// if you want to try your code on the right panel
// remember to export App() component like below

export function App() {

  // test behavior: trigger reredner in state
  const [state, setState] = useState('starting value')
  const render = useIsFirstRender()
  useEffect(() => {
    console.log(render)
    const timeoutId = setTimeout(() => {
      setState('Delayed message after 2 seconds!');
      const render2 = useIsFirstRender()
      console.log(render2)
    }, 2000);

    // Cleanup function to clear the timeout if the component unmounts
    return () => clearTimeout(timeoutId);
  })
  return <div>{state}</div>
}


