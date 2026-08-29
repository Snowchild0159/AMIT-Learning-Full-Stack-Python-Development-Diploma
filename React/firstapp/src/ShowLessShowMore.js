import { useState } from "react"
function ShowLessShowMore({data}){
  let [Show , setShow] = useState(true)
  function toggleShow(){
    setShow(!Show)
  }
  
  return <div>
    <p>
        {
            Show ? data : data.slice(0 , 20) + (data.length > 20 ? "..." : "")
        }
    </p>
    <p>
        {
          data.length > 20 && <button onClick={toggleShow}>Show{Show ? "less" : " more"}  </button>
        }
    </p>

   
  </div>
}

export default ShowLessShowMore