import './styles.css';

import {useState, useEffect, Component} from 'react'


// https://legacy.reactjs.org/docs/hooks-effect.html
export default function App() {
  
  // storing blog post states
  const [blogPosts, setBlogPosts] = useState([]);

  // on load
  useEffect(() => {
    const fetchData = async () => {
      try {
        const ids = await fetch('https://hacker-news.firebaseio.com/v0/jobstories.json')
          .then(response => response.json());

        const result = await Promise.all(
          ids.map(async (id) => {
            const data = await fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`)
              .then(response => response.json());
            return data;
          })
        );

        console.log('Fetched IDs:', ids);
        console.log('Fetched Posts:', result);

        // Remove the first element of the result array
        result.shift();

        setBlogPosts(result);
        console.log('Updated Posts:', result);
      } catch (err) {
        console.log(err);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Title</th>
          </tr>
        </thead>
        <tbody>
          {blogPosts.length > 0 ? (
            blogPosts.map((item) => (
              <tr key={item.id}>
                <td>{item.title}</td>
                <td>{item.time}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="1">No posts available</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
