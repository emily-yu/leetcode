// import { useRef, useState } from "react"
import { useState } from "react"

export function useToggle(on: boolean): [boolean, () => void] {
  // your code here

  /*
    // default not toggled
    const isToggled = useRef(false)

    // access function
    const setToggle = () => {
      isToggled.current = !(isToggled.current)
      console.log(isToggled)
    }
    // return toggle value, and the access function
    return [isToggled.current, setToggle]
  */

  // the above not necessary because goal is to maintain state, not retain a reference to the value - it's reset every time creating a new instance
  // https://www.reddit.com/r/reactjs/comments/ry256i/can_someone_please_explain_the_difference_between/
  const [state, setState] = useState(on)
  const toggleFunction = () => {
    setState(!state)
  }
  return [state, toggleFunction]
}


// if you want to try your code on the right panel
// remember to export App() component like below

export function App() {
  const [on, toggle] = useToggle(false)
  console.log(on)
  toggle()
  console.log(on)
  return <p>{on}</p>
}


