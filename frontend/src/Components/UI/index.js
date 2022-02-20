import React from "react"
import './style.css';

// import components
import {Header} from "../Header"
import {Content} from "../Content"

import { Link } from "react-router-dom";

class UI extends React.Component {

    // constructor(props) {
    //     super(props);
    // }

    render() {
        return (

            <div className="App">
                <Header/>
                <Content/>

                {/* <footer>
                    Footer
                </footer> */}
            </div>
        )
    }
        

}

export {UI};