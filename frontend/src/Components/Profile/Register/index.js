import React from "react"
import './style.css'
import {Header} from "../../Header"

import { Link } from "react-router-dom"

export class RegisterPageComponent extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            username: "",
            password:"",
            password2:"",
            email:"",
            name:""
        }
        
    }

    
    handleNameInput = event => this.setState({name: event.target.value})
    handleEmailInput = event => this.setState({email: event.target.value})
    handleUsernameInput = event => this.setState({username: event.target.value})
    handlePasswordInput = event => this.setState({password: event.target.value})
    handlePasswordInput2 = event => this.setState({password2: event.target.value})


    // we will add validators later



    render() {
        return (


            <div className="login_page_main">
                <Header/>
                <form className="login_form">
                    <h2 className="form_title">Register</h2>

                    {/* <div className="form-control"> */}

                        <label htmlFor="name">Full name:</label>
                        <input autoFocus type="text" id="name"
                        value={this.state.name}
                        onChange={this.handleNameInput}
                    />
                    {/* </div> */}

                    {/* <div className="form-control"> */}
                        <label htmlFor="username">Username:</label>
                        <input autoFocus type="text" id="username"
                        value={this.state.username}
                        onChange={this.handleUsernameInput}
                    />
                    {/* </div> */}

                    {/* <div className="form-control"> */}
                        <label htmlFor="email">Email:</label>
                        <input autoFocus type="text" id="email"
                        value={this.state.email}
                        onChange={this.handleEmailInput}
                    />
                    {/* </div> */}

                    {/* <div className="form-control"> */}
                        <label htmlFor="password">Password:</label>
                        <input autoFocus type="password" id="password"
                        value={this.state.password}
                        onChange={this.handlePasswordInput}
                        />

                        
                    {/* </div> */}

                    <label htmlFor="confirm-password">Confirm your password:</label>
                    <input autoFocus type="password" id="confirm-password"
                    value={this.state.password2}
                    onChange={this.handlePasswordInput2}
                    />


                    <span>Already an user? <Link to="/register">Login</Link></span>

                    <button type="submit" onSubmit={this.props.submitFunction}>Submit</button>
                </form>
            </div>
        )
    }



}