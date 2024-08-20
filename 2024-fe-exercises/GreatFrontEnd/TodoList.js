/*
    https://www.greatfrontend.com/questions/user-interface/todo-list
*/

import './styles.css';

export default function App() {
  const removeItem = (e) => {
    let listItem = e.target.parentNode;
    //get the parent of the list item (ul)
    let list = listItem.parentNode;
    //remove the child from the list         
    list.removeChild(listItem);
  }
  const addItem = () => {
    const text = document.getElementById('input')
    const base = document.getElementsByTagName('ul')[0]

    // delete on new buttons not triggering - need to set manually
    // better version of adding innerHTML, https://stackoverflow.com/questions/7327056/appending-html-string-to-the-dom
    base.insertAdjacentHTML('beforeend', `<li><span>${text.value}</span><button id="addDelete">Delete</button></li>`);
    const button = document.getElementById('addDelete')
    console.log(button)
    // https://stackoverflow.com/questions/6956258/adding-onclick-event-handler-to-dynamically-added-button
    button.addEventListener("click", removeItem)

  }

  return (
    <div>
      <h1>Todo List</h1>
      <div>
        <input id="input" type="text" placeholder="Add your task" />
        <div>
          <button onClick={addItem}>Submit</button>
        </div>
      </div>
      <ul>
        <li>
          <span>Walk the dog</span>
          <button onClick={removeItem}>Delete</button>
        </li>
        <li>
          <span>Water the plants</span>
          <button onClick={removeItem}>Delete</button>
        </li>
        <li>
          <span>Wash the dishes</span>
          <button>Delete</button>
        </li>
      </ul>
    </div>
  );
}
