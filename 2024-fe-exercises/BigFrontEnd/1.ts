// https://bigfrontend.dev/react/The-React-Counter

import React, { useState } from 'react'

export function App() {
  const [count, setCount] = useState(0)

  const add = () => {
    setCount(count + 1)
  }
  const subtract = () => {
    setCount(count - 1)
  }
  return (
    <div>
      <button onClick={subtract} data-testid="decrement-button">-</button>
      <button onClick={add}data-testid="increment-button">+</button>
      <p>clicked: {count}</p>
    </div>
  )
}

// run your code by clicking the run button on the right




