import React from 'react';
import axios from 'axios'
// import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import NavBar from './components/Navbar'
import UsersList from './components/Users'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        const users = response.data
        this.setState(
          {
            'users': users
          }
        )
      }).catch(error => console.log(error))
  }

  render() {
    return (
      
      <div>
        <NavBar sticky="top"/>
        <UsersList users={this.state.users} /> 
      </div>
    )
  }
}
export default App;
