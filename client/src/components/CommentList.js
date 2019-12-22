import React, { useState } from "react";
import { Comment, Header, Form, Button, Icon, Input } from "semantic-ui-react";

const CommentForm = () => {
    const [commentBody, setCommentBody] = useState("");

    return (
        <Form reply>
            <Form.TextArea
                // style={{ width: "100%" }}
                value={commentBody}
                onChange={e => {
                    setCommentBody(e.currentTarget.value);
                }}
            />
            <Button
                content="Post Comment"
                labelPosition="left"
                icon="edit"
                primary
                onClick={async () => {
                    const response = await fetch(this.state.url, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ body: commentBody })
                    });
                }}
            />
        </Form>
    );
};

export default class CommentList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            commentBody: "",
            post_id: props.post_id,
            comments: [],
            url:
                "http://api.catpic.margiris.site:5000/post/" +
                props.post_id +
                "/comment"
        };
    }

    componentDidMount() {
        fetch(this.state.url).then(response =>
            response.json().then(data => {
                this.setState({ comments: data.comments });
            })
        );
    }

    render() {
        const { comments, commentBody } = this.state;

        return (
            <Comment.Group>
                <Header as="h3" dividing>
                    Comments
                </Header>
                {comments.map(comment => {
                    return (
                        <Comment key={comment.id}>
                            <Comment.Content>
                                <Comment.Author>
                                    {comment.author}
                                </Comment.Author>
                                <Comment.Metadata>
                                    <div>{comment.posted_time}</div>
                                    <div>
                                        <Icon name="heart" />
                                        {comment.rating}
                                    </div>
                                </Comment.Metadata>
                                <Comment.Text>{comment.body}</Comment.Text>
                            </Comment.Content>
                        </Comment>
                    );
                })}
                <CommentForm />
            </Comment.Group>
        );
    }
}
