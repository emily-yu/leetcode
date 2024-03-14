import React from "react";
import { fetchJoke, IJoke } from "../components/context";

export const JokeComponent: React.FC<IJoke> = ({ data }) => {
  return (
    <div>
      <p>{data.joke}</p>
      <p>ID: {data.id}</p>
    </div>
  );
};
