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
        }


        // infinite scroll component logic, check every time you scroll
        window.onscroll = debounce(() => {
            const {
                getPosts
            } = this;
            // if it has reached the bottom of the page, get more posts given the next page
            // which is stored as a state variable
            if (window.innerHeight + document.documentElement.scrollTop === document.documentElement.offsetHeight) {
                
                this.getPosts(this.state.page);
              }
            //   add some timing to make the wait slimmer
            }, 200);
        }
    
    // at page reload give the first n posts
    componentDidMount() {
        this.getPosts()
    }

    // get n more posts
    getPosts(page=1) {
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