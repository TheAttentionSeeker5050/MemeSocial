import React from "react"
import './style.css';

// import the contexts
import {LoginContext} from "../../../Contexts/login_modal"

class LoginModalComponent extends React.Component {
    render() {
      let props = this.props;
      let toggle_modal = this.context;
      return (
        <section className="login_modal_container"
            {...props}
        >
            <form>
                <label for="username">Username:</label>
                <input type="text" id="username"/>

                <label for="password">Password:</label>
                <input type="password" id="password"/>

                <button type="submit">Submit</button>
            </form>

        </section>
      );
    }
  }
  LoginModalComponent.contextType = LoginContext;
  
  export {LoginModalComponent};