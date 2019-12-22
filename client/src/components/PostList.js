import React from "react";
import { Container } from "semantic-ui-react";

import Post from "./Post";

class PostList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            posts: []
        };
    }

    componentDidMount() {
        fetch("http://api.catpic.margiris.site:5000/post").then(response =>
            response.json().then(data => {
                this.setState({ posts: data.posts });
            })
        );
    }

    render() {
        return (
            <Container style={{ marginTop: 30, marginBottom: 40 }}>
                {this.state.posts.map(post => {
                    return <Post key={post.id} post={post} />;
                })}
            </Container>
        );
    }
}

export default PostList;
