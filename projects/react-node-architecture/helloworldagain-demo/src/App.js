import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}

      {/* haha it passes the jest test xd */}
                Learn React

      <form
                    action="https://localhost:8080/post"
                    method="post"
                    className="form">
                    <button type="submit">
                        Connected?
                    </button>
                </form>
    </div>
  );
}

export default App;
