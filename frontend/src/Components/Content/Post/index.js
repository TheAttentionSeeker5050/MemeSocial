import { post } from "superagent"
import React from "react"
import './style.css';

class Post extends React.Component {

    constructor(props) {
        super(props)
        // this.state = {
        //     usernames = []
        // }

    }

    // getUsername(pk) {
    //     fetch(`http://127.0.0.1:8000/api/user/${pk}`)
    //         .then(response => response.json())
    //         .then(data => {
    //             this.setState({usernames})
    //         })
    //         .catch(error => console.log(error))
    // }

    

    render() {

        return (
            <div className="post_container">

                            <h3 className="post_title">{this.props.post.title}</h3>
                            <p className="post_username">{this.props.post.posted_by}</p>
                            <p className="post_content">{this.props.post.content}</p>
                            <img src={this.props.post.meme}  alt="meme" className="meme_caption"/>
                            
                            <div className="post_footer">
                                <img src="https://img.icons8.com/external-becris-lineal-becris/16/fb5607/external-like-mintab-for-ios-becris-lineal-becris.png" className="like_img" alt="like"/>
                                <img src="https://img.icons8.com/external-becris-lineal-becris/16/fb5607/external-dislike-mintab-for-ios-becris-lineal-becris.png" className="dislike_img" alt="Dislike"/>
                                <img src="https://img.icons8.com/material-outlined/16/fb5607/comments--v1.png" className="comment_img" alt="Comment"/>
                                

                            </div>
                        </div>
        )
    }
}

export {Post}