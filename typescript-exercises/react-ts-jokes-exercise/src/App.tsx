import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

// Pages
import Main from "./pages/Main";
import Favorites from "./pages/Favorites";

export default function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/favorites">
          <Favorites />
        </Route>
        <Route path="/">
          <Main />
        </Route>
      </Switch>
    </Router>
  );
}
