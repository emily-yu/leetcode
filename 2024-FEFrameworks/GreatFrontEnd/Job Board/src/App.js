import './styles.css';

import {useState, useEffect, Component} from 'react'


// https://legacy.reactjs.org/docs/hooks-effect.html
export default function App() {
  
  // storing blog post states
  const [blogPosts, setBlogPosts] = useState();

  // cannot use this, because not a class
  // componentDidMount() {
  //   getData()
  // }

  // on load
  useEffect(() => {
    // getData()
  })
// {JSON.stringify(blogPosts)}
  return <div><CardWrapper/></div>;
}

// using a separate Card component (componentDidMount, componentDidUpdate)
class CardWrapper extends Component {
  constructor(props) {
    super(props)
    this.state = {
      blogPosts: []
    }
  }
  componentDidMount() {
    console.log("mounted")
    
    console.log('hello')
    fetch(`https://hacker-news.firebaseio.com/v0/jobstories.json`)
        .then(response => response.json())
        .then(data => {
          console.log("arrivals")
          console.log(data)
          this.setState({
            blogPosts: data
          })
        })
        .catch(err => {
          console.log(err)
        })
  }
  
  // componentDidUpdate() {

  // }

  render() {
    return (
      <>
        <ul>
          {
            // this.state.blogPosts
            this.state.blogPosts.map((item) => <li>{JSON.stringify(item)}</li>)
          }
        </ul>
        <div>Card: asdf</div>
      </>
    )
  }
}