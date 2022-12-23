import React from "react"
import { Routes, Route, BrowserRouter } from "react-router-dom"

import PonyNote from "./components/PonyNote";
import NotFound from "./components/NotFound";

import { Provider } from "react-redux";
import { createStore } from "redux";
import loggerApp from "./reducers";


let store = createStore(loggerApp);

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <BrowserRouter>
          <Routes>
            <Route exact path="/" element={<PonyNote/>} > </Route>
            <Route exact path="*" element={<NotFound/>} > </Route>
          </Routes>
        </BrowserRouter>
      </Provider>
    </div>
  )
}

export default App
