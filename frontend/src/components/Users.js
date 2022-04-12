import React from 'react'
import { Table } from 'react-bootstrap';

const UserItem = ({ user }) => {
    return (
        <tbody>
            <tr>
                <td>
                    {user.username}
                </td>
                <td>
                    {user.first_name}
                </td>
                <td>
                    {user.last_name}
                </td>
                <td>
                    {user.email}
                </td>
                <td>
                    {user.url}
                </td>
            </tr>
        </tbody>
    )
}

const UsersList = ({ users }) => {
    return (
        <Table striped bordered hover>
            <thead>
                <th>
                    username
                </th>
                <th>
                    first_name
                </th>
                <th>
                    last_name
                </th>
                <th>
                    email
                </th>
                <th>
                    url
                </th>
            </thead>
            {users.map((user) => <UserItem user={user} />)}
        </Table>
    )
}
export default UsersList