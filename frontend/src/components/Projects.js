import React from 'react'
import { Table } from 'react-bootstrap';
import { Link, useParams } from 'react-router-dom'
import axios from 'axios'


const ProjectUsers = ({ projectUser }) => {
    return (
        <p>
            {projectUser.firstName} {projectUser.lastName} {projectUser.email}
        </p>
    )
}

const ProjectItem = ({ project }) => {
    return (
        <tbody>
            <tr>
                <td>
                    <Link to={`${project.id}`}>{project.name}</Link>
                </td>
                <td>
                    <a href={project.link} target="_blank">{project.link}</a>
                </td>
                <td>
                    {project.users.map((user) => <ProjectUsers projectUser={user} />)}
                </td>
            </tr>
        </tbody>
    )
}

const ProjectsTeble = ({ projects }) => {
    return (
        <Table striped bordered hover>
            <thead>
                <th>
                    Название проекта
                </th>
                <th>
                    Ссылка на репо
                </th>
                <th>
                    Пользователи проекта
                </th>
            </thead>
            {projects.map((project) => <ProjectItem project={project} />)}
        </Table>
    )
}


export default class ProjectsList extends React.Component {
    state = {
        'projects': []
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState({ 'projects': projects })
            }).catch(error => console.log(error))
    }

    render() {
        return (
            ProjectsTeble({ projects: this.state.projects })
        )
    }
}
