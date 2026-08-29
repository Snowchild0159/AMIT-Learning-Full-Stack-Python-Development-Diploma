import React, { useState } from 'react'

export default function Form() {
    const [name, setName] = useState("")
    function handleName(e){
        if(e.target.value.length > 3){
            return
        }
        setName(e.target.value)
    }
  return (
    <div>
        <form>
         <div>
        <label htmlFor='first_name'>First Name</label>
        <input onChange={handleName} value={name} id='first_name' placeholder='please enter your name'></input>
         </div>
         <div>
            what you enter : {name}
         </div>
        </form>
    </div>
  )
}
