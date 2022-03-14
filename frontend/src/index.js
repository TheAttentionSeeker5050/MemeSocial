import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';
import {RegisterPageComponent} from "./Components/Profile/Register/index"

// import the ui
import {UI} from "./Components/UI"


// import the router library
import { BrowserRouter, Route, Routes } from "react-router-dom"

ReactDOM.render(
  <BrowserRouter>
    <Routes>

      <Route path="/register" element={<RegisterPageComponent/>}></Route>
      <Route path="/Profile" element={<h1>Profile page</h1>}></Route>

      <Route path="/post/id" element={<h1>display a post</h1>}></Route>

      <Route path="/create" element={<h1>create a new meme page</h1>}></Route>

      <Route path="/feed">
        <Route path="shuffle" element={<h1>Shuffle page</h1>}></Route>
        <Route path="find" element={<h1>Find page</h1>}></Route>

      </Route>
      <Route path="/" element={<UI />}></Route>




    

    </Routes>
  </BrowserRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
