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
        this.unlisten = this.props.history.listen((location, _) => {
            this.setState({ state: this.state });
        });

        const url = process.env.REACT_APP_API_URL + "/post";

        fetch(url).then(response =>
            response.json().then(data => {
                this.setState({ posts: data.posts });
            })
        );
    }

    componentWillUnmount() {
        this.unlisten();
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
