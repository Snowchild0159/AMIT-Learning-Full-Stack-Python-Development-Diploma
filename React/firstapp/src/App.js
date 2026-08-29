import logo from './logo.svg';
import './App.css';
import List from './List';
import ShowLessShowMore from './ShowLessShowMore';
import ShowAlert from './ShowAlert';
import Form from './Form';
import { useState } from 'react';
import TableOfData from './TableOfData';
import { Route , Routes} from 'react-router';
import AboutPage from './pages/AboutPage';

function App() {
  const[Show , setShow] = useState(false)
  function handleAlert(){
    setShow(true)

    setTimeout(() => {
      setShow(false)
      
    }, 2000);
  }

  function removeAlert(){
    setShow(false)
  }
  return (
    <div className="App">
     <ul>
      <Routes>
        <Route path='/home' element ={<TableOfData/>}/>
        <Route path='/' element ={<TableOfData/>}/>
        <Route path='/about' element ={<AboutPage/>}/>
      </Routes>
      <Form></Form>
      <button onClick={handleAlert}>alert</button>
      {Show && <ShowAlert func = {removeAlert}></ShowAlert>}
     </ul>
    </div>
  );
}

export default App;
