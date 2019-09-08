import React from 'react';
import './App.css';

import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';

import Home from './pages/Home';

const App = () => {
  return (
    <Router>
      <div className="App">
        <nav>
          {/*
            Note the two different types of whitespace
            or you can use the react-add-space package
          */}

          <header>
              <h1>Django Blog</h1>
          </header>

          <Link to="/">Home</Link>
          &nbsp;
          <Link to="/procedures">Procedures</Link>
          {' '}
          <Link to="/contact">Contact</Link>
        </nav>

        <Switch>
          {/* <Route path="/procedures/:id" render={ (props) =>
            <Procedure {...props} />
          } /> */}

          {/* <Route path="/procedures" render={ (props) =>
            <Procedures {...props} />
          } /> */}

          {/* <Route path="/contact" render={ (props) =>
            <Contact phone_number="1-800-MY-TEETH" {...props} />
          } /> */}

          <Route path="/" component={Home} />
        </Switch>

        <footer>
          <p>© Adam Weiler - 2019</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
