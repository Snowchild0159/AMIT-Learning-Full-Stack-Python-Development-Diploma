import { useState } from "react"
function List (){
  let [counter , setCounter] = useState(0)
  function handleClick(){
    setCounter(counter + 1 )
  }
  function handleDecrement(){
    setCounter(counter - 1 )
  }
  function handleRest(){
    setCounter(0)
  }
  return <div>
    <p>
        Counter : {counter}
    </p>

    <button onClick={handleClick}>Increment</button>
    <button onClick={handleDecrement}>Decrement</button>
    <button onClick={handleRest}>Reset</button>
  </div>
}

export default List