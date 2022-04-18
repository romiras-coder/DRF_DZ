import React from 'react'
import { Table } from 'react-bootstrap';
import { Link, useParams } from 'react-router-dom'
import axios from 'axios'



const Item = ({ item }) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
        </tr>
    )
}


const ProjectItem = ({ items }) => {
    let { id } = useParams();
    let filtered_items = items.filter((item) => item.author.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUTHOR</th>
            </tr>
            {filtered_items.map((item) => <Item item={item} />)}
        </table>
    )
}
export default ProjectItem
