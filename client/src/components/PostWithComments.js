import React from "react";
import { Container } from "semantic-ui-react";

import Post from "./Post";
import CommentList from "./CommentList";

class PostWithComments extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            post_id: this.props.match.params.post_id,
            post: Object()
        };
    }

    componentDidMount() {
        this.unlisten = this.props.history.listen((location, _) => {
            this.setState({ post_id: location.pathname.slice(6) });
            this.fetch();
        });

        this.fetch();
    }

    fetch() {
        const url =
            "http://api.catpic.margiris.site:5000/post/" + this.state.post_id;

        fetch(url).then(response =>
            response.json().then(data => {
                this.setState({ post: data.post });
            })
        );
    }

    componentWillUnmount() {
        this.unlisten();
    }

    render() {
        const { post, post_id } = this.state;
        console.log(post);

        return (
            <Container className="main-container">
                <Post post={post} />
                <CommentList post_id={post_id} />
            </Container>
        );
    }
}

export default PostWithComments;
