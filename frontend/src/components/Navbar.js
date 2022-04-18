import React from 'react';
import { LinkContainer } from 'react-router-bootstrap'
import { Nav, Navbar, Container } from 'react-bootstrap';
import { BrowserRouter, Route, Routes, useLocation, useParams } from 'react-router-dom'
import UsersList from './Users'
import ProjectsList from './Projects'
import ItemsDate from './ProjectItem'
import TodoList from './Todo'


const NotFound404 = () => {
    var location = useLocation()

    return (
        <div>
            Page "{location.pathname}" not found
        </div>
    )
}


export default function NaviBar() {

    return (
        <BrowserRouter>
            <Navbar bg="light" expand="lg">
                <Container>
                    <Navbar.Brand href="#home">Навигация</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">

                            <LinkContainer to="/">
                                <Nav.Link>Домой</Nav.Link>
                            </LinkContainer>

                            <LinkContainer to="/Users">
                                <Nav.Link>Пользователи</Nav.Link>
                            </LinkContainer>

                            <LinkContainer to="/Projects">
                                <Nav.Link>Проекты</Nav.Link>
                            </LinkContainer>

                            <LinkContainer to="/Todos">
                                <Nav.Link>Заметки</Nav.Link>
                            </LinkContainer>

                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            <Routes>
                <Route exact path='/Users' element={<UsersList />} />
                <Route exact path='/Projects' element={<ProjectsList />} />
                <Route exact path='/Projects/:id'>

                </Route>
                <Route exact path='/Todos' element={<TodoList />} />
                <Route path='*' element = {<NotFound404 />} />
            </Routes>
        </BrowserRouter>
    )
};