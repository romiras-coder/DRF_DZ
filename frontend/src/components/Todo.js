import React from 'react'
import { Table } from 'react-bootstrap';
import axios from 'axios'


// const ProjectUsers = ({ projectUser }) => {
//     return (
//         <p>
//             {projectUser.firstName} {projectUser.lastName} {projectUser.email} 
//         </p>
//     )
// }

const TodoItem = ({ todo }) => {
    return (
        <tbody>
            <tr>
                <td>
                    {todo.project.name}
                </td>
                <td>
                    {todo.text}
                </td>
                <td>
                    {todo.status}
                </td>
            </tr>
        </tbody>
    )
}

const TodosTeble = ({ todos }) => {
    return (
        <Table striped bordered hover>
            <thead>
                <th>
                    Проект
                </th>
                <th>
                    Текст заметки
                </th>
                <th>
                    Статус
                </th>
            </thead>
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </Table>
    )
}

export default class TodoList extends React.Component {
    state = {
        'todos': []
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data.results
                this.setState({ 'todos': todos })
            }).catch(error => console.log(error))
    }
    render() {
        return (
            TodosTeble({ todos: this.state.todos })
        )
    }
}
