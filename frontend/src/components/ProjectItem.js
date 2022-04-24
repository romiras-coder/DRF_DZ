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


// const ProjectItem = ({ items }) => {
//     let { id } = useParams();
//     // let filtered_items = items.filter((item) => item.id == id)

//     return (
//         <table>
//             <tr>
//                 <th>ID </th>
//                 <th>NAME</th>
//                 <th>AUTHOR</th>
//             </tr>
//             {<Item item={id} />}
//         </table>
//     )
// }
// export default ProjectItem


export default class ProjectItem extends React.Component {
    
    state = {
        'projects': []
    }
    
    componentDidMount() {
        // let { id } = useParams();
        // console.log(id)
        axios.get(`http://127.0.0.1:8000/api/projects/`)
            .then(response => {
                const projects = response.data.results
                this.setState({ 'projects': projects })
            }).catch(error => console.log(error))
    }

    
    render() {
        return (
            
            <div>
                Page "{this.props.params}" not found
            </div>
        )
    }
}