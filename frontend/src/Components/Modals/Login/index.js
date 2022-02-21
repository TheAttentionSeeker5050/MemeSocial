import React from "react"
import './style.css';

import ReactDOM from 'react-dom'

// // import the contexts
// import {LoginContext} from "../../../Contexts/login_modal"


class LoginModalComponent extends React.Component {

    constructor(props) {
      super(props);
      
      
    }


    render() {
      const showHideClassName = this.props.show ? "modal show_modal" : "modal hide_modal";
      
      return (
        <section className={showHideClassName}>   
            <div className="modal_main">
              
              <form className="login_form" >
                  <h2 className="form_title">Login</h2>


                  <label htmlFor="username">Username:</label>
                  <input autoFocus type="text" id="username"
                  value={this.props.username}
                  onChange={this.props.onUsernameInput}
                  />

                  <label htmlFor="password">Password:</label>
                  <input autoFocus type="password" id="password"
                  value={this.props.password}
                  onChange={this.props.onPasswordInput}
                  />

                  <button type="submit" onClick={this.props.attemptLogin}>Submit</button>
              </form>
            </div>

        </section>
      );
    }
  }
  // LoginModalComponent.contextType = LoginContext;
  
  export {LoginModalComponent};