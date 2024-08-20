import React, { useEffect, useState } from "react";
import { useContext } from "react";
import { Link } from "react-router-dom";
import "../components/main.css";

// https://www.freecodecamp.org/news/context-api-in-react/
import { FavoritesList } from "../components/context.tsx";
import { fetchJoke, IJoke } from "../components/context";
import { JokeComponent } from "../components/Joke.tsx";
import axios from "axios";

// Joke API URL
// https://icanhazdadjoke.com/

/* checkpoint 3: update page based on api request */
const Main: React.FC = () => {
  // base: USESTATE<TYPE | BASEVALUE>
  const [joke, setJoke] = useState<IJoke | null>(null);
  const loading = false;
  // const { text, setText } = useContext(FavoritesList);
  // const { favoritesList } = useContext(FavoritesList);

  // async function jokeClick() {
  //   try {
  //     const joke: IJoke = await fetchJoke();
  //     console.log("Fetched joke:", joke);
  //     setText(joke.joke);
  //   } catch (error) {
  //     console.error("An error occurred:", error);
  //   }
  // }

  /*
    TLDR; RUNS ONCE IN THE BEGINNING
    useEffect is used to fetch data from an API after the component renders. 
    The effect runs once after the initial render ([] as the dependency array), and updates the data state with the fetched data.
  */
  // useEffect(() => {
  const fetchJoke = async () => {
    try {
      // setLoading(true);
      const response = await axios.get<IJoke>("https://icanhazdadjoke.com/", {
        headers: {
          Accept: "application/json",
        },
      });
      setJoke(response.data);
    } catch (error) {
      console.error("Error fetching joke:", error);
    } finally {
      // setLoading(false);
    }
  };

  // fetchJoke();
  // }, []);

  return (
    <section class="main">
      {/* <h1>beep: {text}</h1> */}
      <h1>Joke Generator</h1>
      <button onClick={fetchJoke}>Joke Please!</button>
      <section class="result">
        <div>
          text
          {loading ? (
            <p>Loading...</p>
          ) : joke ? (
            <JokeComponent data={joke} />
          ) : (
            //   <p>{joke.joke}</p>
            //   <p>ID: {joke.id}</p>
            // </div>
            <p>No joke available</p>
          )}
        </div>
        <p>test2</p>
      </section>
      {/* <h2>Favorite Jokes</h2>
      <ul>
        {favoritesList.map((joke: IJoke) => (
          <li key={joke.id}>{joke.joke}</li>
        ))}
      </ul> */}
      <hr />
    </section>
  );
};

export default Main;
