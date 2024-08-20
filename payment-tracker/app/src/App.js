import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react'

function App() {
  const [a, setA] = useState();

  const setterA = (value) => {
    setA(value)
    console.log(value)
  }

  useEffect(()=> {
    console.log("hello")
  })
  return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
      <form>
        <input type="text" onChange={e => setA(e.target.value)}></input>
        <input type="text" onChange={e => setterA(e.target.value)}></input>
        <input type="text"></input>
      </form>
    // </div>
  );
}

export default App;
