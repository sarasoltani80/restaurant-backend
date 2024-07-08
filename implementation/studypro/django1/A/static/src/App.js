import './App.css';
import Home from '../src/components/Home';
import { Route, Switch } from 'react-router-dom/cjs/react-router-dom.min';
import { Redirect } from 'react-router-dom/cjs/react-router-dom.min';
import Register from './components/Register';
import Login from './components/Login';

function App() {
  return (
    <Home>
      <Switch>
        <Route path='/' exact>
          <Redirect to='/home' />
        </Route>
        <Route path='accounts/register'>
          <Register />
        </Route>
        <Route path='accounts/login'>
          <Login />
        </Route>
      </Switch>
    </Home>
  );
}

export default App;
