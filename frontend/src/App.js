import React from 'react';
import './App.css';

import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom'

const App = () => {
  return (
    <Router>
      <div className="App">
        <h1>Hello!</h1>
      </div>
    </Router>
  );
}

export default App;
