import React from "react";
import { Image, Card, Icon, Modal } from "semantic-ui-react";
import { NavLink } from "react-router-dom";

import CommentList from "./CommentList";

class Post extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            post: props.post
        };
    }

    render() {
        const { post } = this.state;
        // var datetime_difference = Date.now() - new Date(post.posted_on);

        return (
            <Card fluid className="Card">
                <Card.Content>
                    <Card.Header>
                        <NavLink to={"/post/" + post.id} className="a">
                            {post.title}
                        </NavLink>
                    </Card.Header>
                </Card.Content>
                <Image
                    src="http://hdqwalls.com/wallpapers/cat-green-eyes-4k-i8.jpg"
                    href={"/post/" + post.id}
                    ui={false}
                />
                <Card.Content>
                    <Card.Meta>
                        <span className="time">
                            <NavLink to={"/user/" + post.author} className="a">
                                {post.author}
                            </NavLink>
                            {" · "}
                            {post.posted_on}
                        </span>
                    </Card.Meta>
                </Card.Content>
                <Modal
                    trigger={
                        <Card.Content extra>
                            <NavLink to="#">
                                <Icon name="comments" />
                                {post.comment_count} comments
                            </NavLink>
                        </Card.Content>
                    }
                >
                    <Modal.Content>
                        <Post post={post} />
                        <CommentList parent={this} post_id={post.id} />
                    </Modal.Content>
                </Modal>
            </Card>
        );
    }
}

export default Post;
