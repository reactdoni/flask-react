import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css';
import React from 'react';
import ReactDOM from 'react-dom';
import NavBar from './components/Navbar';
import CreateRecipePage from './components/CreateRecipe';
import LoginPage from './components/Login';
import SignUpPage from './components/SignUp';
import HomePage from './components/Home';

import {
    BrowserRouter as Router,
    Routes,
    Route
} from 'react-router-dom'

const App=() => {

    return (
        <Router>
        <div className="">
            <NavBar/>
            <Routes>

                <Route path="/create_recipe" element={<CreateRecipePage />}></Route>

                <Route path="/login" element={<LoginPage />}></Route>

                <Route path="/signup" element={<SignUpPage />}></Route>

                <Route path="/home" element={<HomePage />}></Route>

                <Route path="/" element={<HomePage />}></Route>

            </Routes>
        </div>
        </Router>
    )
}

ReactDOM.render(<App/>, document.getElementById('root'))