/*
    https://www.greatfrontend.com/questions/user-interface/contact-form
*/

import './styles.css';
import submitForm from './submitForm';

export default function App() {
  return (
    <form 
      action="https://www.greatfrontend.com/api/questions/contact-form"
      method="post"
      // Ignore the onSubmit prop, it's used by GFE to
      // intercept the form submit event to check your solution.
      onSubmit={submitForm}>
      <input type="text" name="name"/>
      <input type="email" name="email"/>
      <textarea name="message" cols="86" rows ="20"></textarea>
      <input type="submit" value="Send"/>
    </form>
  );
}
