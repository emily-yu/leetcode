import './styles.css';

import {useState, useEffect, Component} from 'react'


// https://legacy.reactjs.org/docs/hooks-effect.html
export default function App() {
  
  // storing blog post states
  const [blogPosts, setBlogPosts] = useState([]);

  // on load
  useEffect(() => {    

    const derp = async() => {
// nested fetches. https://stackoverflow.com/a/57075730
    const ids = await fetch(`https://hacker-news.firebaseio.com/v0/jobstories.json`)
        .then(response => response.json())
        .then(data => {
          // console.log("arrivals")
          console.log(data)
          return data
        }).catch(err => {
          console.log(err)
        })
        let result = []
        for (let item in ids) {
          const data = await fetch(`https://hacker-news.firebaseio.com/v0/item/${item}.json`)
            .then(response => response.json())
            .then(data => {
              // console.log("it's only adding on each rerender: ", data)
              return data
            })
            result.push(data)
            // console.log("curr result:", result)
          }
    
        console.log(ids, result)
        return result
      
    }
    derp().then((data) => {
      console.log("the final:", data)
      setBlogPosts(data)
    })
    
  })
  return <ul>{ blogPosts && JSON.stringify(blogPosts)}</ul>;
}
