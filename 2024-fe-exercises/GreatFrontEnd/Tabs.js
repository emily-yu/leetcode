/*
    https://www.greatfrontend.com/questions/user-interface/tabs
*/
export default function Tabs() {

    let currentTab = 'HTML'
    const swapTab = (e) => {
      console.log(e.target)
  
      const buttons = document.getElementsByTagName('button')
      for (let button of buttons) {
        button.style.color = 'black'
      }
      e.target.style.color = "pink"
  
      const text = document.getElementsByTagName('p')
      // console.log(text)
      for (let elems of text) {
        elems.style.visibility = 'hidden'
      }
      if (e.target.innerHTML == "HTML") {
        text[0].style.visibility = 'visible'
      }
      if (e.target.innerHTML == "CSS") {
        text[1].style.visibility = 'visible'
      }
      if (e.target.innerHTML == "JavaScript") {
        text[2].style.visibility = 'visible'
      }
      // e.target.color = 'blue'
    }
  
    return (
      <div>
        <div>
          <button onClick={swapTab}>HTML</button>
          <button onClick={swapTab}>CSS</button>
          <button onClick={swapTab}>JavaScript</button>
        </div>
        <div>
          <p>
            The HyperText Markup Language or HTML is the
            standard markup language for documents designed to
            be displayed in a web browser.
          </p>
          <p>
            Cascading Style Sheets is a style sheet language
            used for describing the presentation of a document
            written in a markup language such as HTML or XML.
          </p>
          <p>
            JavaScript, often abbreviated as JS, is a
            programming language that is one of the core
            technologies of the World Wide Web, alongside HTML
            and CSS.
          </p>
        </div>
      </div>
    );
  }