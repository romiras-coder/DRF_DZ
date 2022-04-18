import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import NavBar from './components/Navbar'

class App extends React.Component {
  render() {
    return (
      <div>
        <NavBar sticky="top" />
      </div>
    )
  }
}
export default App;
