import React from "react";
import { Container, Loader } from "semantic-ui-react";

import Post from "./Post";

class PostList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            posts: []
        };
    }

    componentDidMount() {
        const url = "http://api.catpic.margiris.site:5000/post";

        fetch(url).then(response =>
            response.json().then(data => {
                this.setState({ posts: data.posts });
            })
        );
    }

    render() {
        const { posts } = this.state;

        return (
            <Container className="main-container">
                <Loader inline="centered" active={posts === []} />
                {posts.map(post => {
                    return <Post key={post.id} post={post} />;
                })}
            </Container>
        );
    }
}

export default PostList;
