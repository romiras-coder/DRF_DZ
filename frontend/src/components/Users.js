import React from 'react'
import { Table } from 'react-bootstrap';
import axios from 'axios'

const UserItem = ({ user }) => {
    return (
        <tbody>
            <tr>
                <td>
                    {user.username}
                </td>
                <td>
                    {user.firstName}
                </td>
                <td>
                    {user.lastName}
                </td>
                <td>
                    {user.email}
                </td>
            </tr>
        </tbody>
    )
}

const UsersTeble = ({ users }) => {
    return (
        <Table striped bordered hover>
            <thead>
                <th>
                    username
                </th>
                <th>
                    firstName
                </th>
                <th>
                    lastName
                </th>
                <th>
                    email
                </th>
            </thead>
            {users.map((user) => <UserItem user={user} />)}
        </Table>
    )
}

export default class UsersList extends React.Component {
    state = {
        'users': []
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results
                this.setState({ 'users': users })
            }).catch(error => console.log(error))
    }
    render() {
        return (
            UsersTeble({ users: this.state.users })
        )
    }
}
