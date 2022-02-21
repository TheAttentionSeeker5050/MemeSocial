import React from "react"
import './style.css';

// import components
import {Header} from "../Header"
import {Content} from "../Content"
// import {LoginModalComponent} from "../Modals/Login"

import { Link } from "react-router-dom";

// import the contexts
// import {LoginContext, login_modal} from "../../Contexts/login_modal"

class UI extends React.Component {

    constructor(props) {
        super(props);
        

        
    }

    

    render() {
        // console.log(this.state.login_show_modal)
        // let login_m = this.context
        return (

            <div className="App">
                <Header {...this.state}/>
                <Content/>
                
                
            </div>
        )
    }
        

}

export {UI};