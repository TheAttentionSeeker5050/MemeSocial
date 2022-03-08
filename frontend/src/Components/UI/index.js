import React from "react"
import './style.css';

// import components
import {Header} from "../Header"
import {Content} from "../Content"
import {LoginModalComponent} from "../Modals/Login"

import { Link } from "react-router-dom";


// import api call
import {login_api} from "../../Api/api_login"

// import the contexts
// import {LoginContext, login_modal} from "../../Contexts/login_modal"




class UI extends React.Component {

    constructor(props) {
        super(props);
        this.showLoginModal = this.showLoginModal.bind(this)
        // this.attemptLogin = this.attemptLogin.bind(this)
        // this.success = this.success.bind(this)

        this.state = {
            loginModalActive:false,
            username:"",
            password:"",
            message:"",
            loggedIn:false
        }
        
    }

    // the response in case of success in sending the login form
    success = async (text) => {
        console.log("user is authenticated")
        await localStorage.setItem("userToken", text.access)
        await localStorage.setItem("username", text)

        window.location = "/"
    }

    attemptLogin = async (element) => {
        // element.preventDefault()
        console.log("login in with", this.state.username)
        await login_api(this.state.username, this.state.password, this.success, (text) => {
            this.setState({message: text.detail})
            localStorage.setItem("error", text.detail)
        })
    }

    handleUsernameInput = event => {
        this.setState({username: event.target.value})
        console.log(this.state.username)
    }
    handlePasswordInput = event => this.setState({password: event.target.value})


    showLoginModal() {
        this.setState({loginModalActive: true})

        // console.log(this.state.loginModalActive)
        console.log("login modal active")

    }

    hideLoginModal() {
        this.setState({loginModalActive: false})
        // console.log(this.state.loginModalActive)
        console.log("login modal inactive")
    }

    

    

    render() {
        // console.log(this.state.login_show_modal)
        // let login_m = this.context
        // console.log(this.state.username)
        return (

            <div className="App">
                <Header showLogin={this.showLoginModal}/>
                <Content message={this.state.message}/>
                <LoginModalComponent 
                    show={this.state.loginModalActive} 
                    username={this.state.username} 
                    password={this.state.password} 
                    submitFunction={this.attemptLogin} 
                    onUsernameInput={this.handleUsernameInput}
                    onPasswordInput={this.handlePasswordInput}
                    />
                
            </div>
        )
    }
        

}

export {UI};