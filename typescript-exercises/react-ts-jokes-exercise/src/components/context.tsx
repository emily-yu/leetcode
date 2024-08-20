import axios from "axios";
import { createContext } from "react";

// use this interface to declare the type of a joke in favorites list
export interface IJoke {
  id: string;
  joke: string;
}

export async function fetchJoke(): Promise<IJoke> {
  try {
    const response = await axios.get("https://icanhazdadjoke.com/", {
      headers: {
        Accept: "text/plain",
      },
    });
    return response.data;
  } catch (error) {
    // Handle error
    console.error("Error fetching joke:", error);
    throw error;
  }
}
/* checkpoint 4: create a new component */
export const FavoritesList = createContext<{ favoritesList: IJoke[] }>({
  favoritesList: [],
});
