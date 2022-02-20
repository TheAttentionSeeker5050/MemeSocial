import './style.css';
import React from "react"

class Header extends React.Component {

    constructor(props) {
        super(props);
        this.handleToggleSeachBar = this.handleToggleSeachBar.bind(this);
        this.state = {
            searchBarActive: false,
        }
    }

    handleToggleSeachBar() {
        this.setState(prev_state => ({
            searchBarActive: !prev_state.searchBarActive
        }))
        console.log(this.state.searchBarActive)
    }

    render() {
        return (
            <header>
                <section className='header_left'>
                
                    <img src="https://img.icons8.com/external-gradak-royyan-wijaya/25/ffffff/external-circle-basic-interface-iii-gradak-royyan-wijaya.png" alt='menu' className='header_left--menu'/>
                    <h1 className="header_left--title">ORANGE SODA </h1>
                    <img src="https://img.icons8.com/external-icongeek26-outline-icongeek26/50/ffffff/external-drink-retro-80s-icongeek26-outline-icongeek26.png"/>
                </section>
                <section className='header_right'>
                    {this.state.searchBarActive===true &&
                        <input type="text" id='meme_search_input'/>
                    }
                    {/* <button > */}
                    <img src="https://img.icons8.com/ios-filled/25/ffffff/search--v1.png" alt='search' className='header_right--search_icon' onClick={this.handleToggleSeachBar}/>
                    {/* </button> */}

                </section>
            </header>
        )
    }
        

}

export {Header};