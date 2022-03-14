import {React} from "react"

class AuthDomMethods extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            username:"",
            password:"",
            message:"",
        }
        this.handlePasswordInput = this.handlePasswordInput.bind(this)
        this.handleUsernameInput = this.handleUsernameInput.bind(this)
    }
    
    // the dom manipulation methods
    handleUsernameInput = event => {
        this.setState({username: event.target.value})
        console.log(this.state.username)
    }
    handlePasswordInput = event => this.setState({password: event.target.value})

    
}

export {AuthDomMethods}