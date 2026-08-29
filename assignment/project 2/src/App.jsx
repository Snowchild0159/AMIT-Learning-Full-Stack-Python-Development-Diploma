import { useEffect, useState } from 'react'
import { host } from './healper'
function App() {

  const [products , setProducts] = useState([])
  const [errorMessage , setErrorMessage] = useState("")


  async function fetchProducts() {

    try {
      const token = localStorage.getItem("token")
      const response = await fetch(`${host}/api/products/` , {
        headers : {
          "Authorization" : `Bearer ${token}`
        }
      })

      const data = await response.json() 

      setProducts(data)
    }catch{
      setErrorMessage("No Data available! ")
    }

  }
  useEffect(()=>{
    fetchProducts()
  } , [])

  return (
    <>
     {products.map(product => <p key={product.id}>{product.name}</p>)}
    </>
  )
}

export default App
