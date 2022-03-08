import React from "react"
import './style.css';

// import axios
import axios from "axios";

// our infinite scroll related imports
import request from 'superagent';
import debounce from 'lodash.debounce';

// import components
import {Post} from "./Post"

class Content extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            page:1,
            posts: [],
            loading:false,
            // show_login_modal:false,
            // show_register_modal:false,
            // show_menu_modal: false
        }
        // this.showLoginModal = this.showLoginModal.bind(this)
        // this.hideLoginModal = this.hideLoginModal.bind(this)


        window.onscroll = debounce(() => {
            const {
                getPosts
            } = this;
            if (window.innerHeight + document.documentElement.scrollTop === document.documentElement.offsetHeight) {
                
                this.getPosts(this.state.page);
              }
            }, 200);
        }
    
    // showLoginModal() {
    //     this.setState({show_login_modal: true})
    // }

    // hideLoginModal() {
    //     this.setState({show_login_modal: false})
    // }

    componentDidMount() {
        this.getPosts()
    }
    getPosts(page=1) {
        // this.setState({ loading: true });
        axios
          .get(
            `http://127.0.0.1:8000/api/posts/?page=${page}`
          )
          .then(res => {
            
            this.setState({ posts: [...this.state.posts, ...res.data.results] });
            // this.setState({ loading: false });
            this.setState({page:this.state.page+1})
          });
      }


    

    render() {

        const loadingCSS = {
            height: "100px",
            margin: "30px"
          
        }

        const loadingTextCSS = { display: this.state.loading ? "block" : "none" };
        return (
            <main >
                <section className="top_feed_menu">
                    <span>Trending</span>
                    <span>Most Viewed</span>
                    <span>Recent</span>
                </section>

                <section className="message_section">{this.props.message}</section>
                

                <section className="feed_container" style={{minHeight:"500px"}}>
                    {this.state.posts.map( post =>
                        <Post
                        post={post}/>
                        
                        
                    )}
                </section>

                

            </main>
        )
    }
        

}

export {Content}