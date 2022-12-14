import React from "react"
import { Routes, Route, BrowserRouter } from "react-router-dom"

import PonyNote from "./components/PonyNote";
import NotFound from "./components/NotFound";


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<PonyNote/>} > </Route>
          <Route exact path="*" element={<NotFound/>} > </Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
