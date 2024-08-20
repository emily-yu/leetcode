import './styles.css';

export default function App() {

  const checkInput = () => {
    const userInput = document.forms["inputForm"]["loanAmount"].value
    // var userInput = document.getElementById('input').value;
    if(!isNaN(userInput)){
        console.log("Is a number");
    }
    else{
        console.log("Is not a number");
    }
  }

  return (
    <form name="inputForm" action='' method=''>
      <input onChange={checkInput} name="loanAmount" type="text" />
      <input name="interestRate" type="number" />
      <input name="loanTerm" type="number" />
    </form>
  );
}
