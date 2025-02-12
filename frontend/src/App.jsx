import './App.css'
import { AnimatePresence } from "framer-motion";
import { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useLocation } from "react-router-dom";
import axios from "axios";
import Login from "./components/Login";
import Navbar from "./components/Navbar";
import AboutUs from "./pages/AboutUs"
import NoteFound from "./pages/404";


const AnimatedRoutes = () => {
  const location = useLocation();
  return (
    <AnimatePresence mode='wait'>
      <Routes location={location} key={location.pathname}>
        <Route path='/login' element={<Login/>}></Route>
        <Route path='/about' element={<AboutUs/>}></Route>
        <Route path='/' element={<Home/>}></Route>
        <Route path='*' element={<NoteFound/>}></Route>
      </Routes>
    </AnimatePresence>
  )
}

// to do
// componente home 
function Home() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        setError("Error al conectarse al backend:" + error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>{loading}</div>
  }
  if (error) {
    return <div>{error}</div>
  }
  return (
    <div>
      <h1>Data de usuarios de django</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>{JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );

}


function App() {

  return (
    <Router>
      <Navbar />
        <div className="container mt-4">
          <div className="row">
            <div className="col">
              <AnimatedRoutes/>
            </div>
          </div>
        </div>
    </Router>
  )
}

export default App
