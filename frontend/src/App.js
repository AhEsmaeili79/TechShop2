import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from './components/Signup';
import Login from './components/Login';
import Home from './components/Home'; // You can add other components here

const App = () => {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>React Django Authentication</h1>
          <nav>
            <ul>
              <li><a href="/signup">Sign Up</a></li>
              <li><a href="/login">Login</a></li>
              <li><a href="/">Home</a></li>
            </ul>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/" element={<Home />} /> {/* Default route or home page */}
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
