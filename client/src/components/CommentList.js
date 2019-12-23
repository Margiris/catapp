import React from "react";
import {
    Comment,
    Header,
    Form,
    Button,
    Icon,
    Container
} from "semantic-ui-react";

class CommentForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            postRef: props.postRef,
            parent: props.parent,
            commentBody: "",
            loggedIn:
                localStorage.getItem("jwtToken") !== null &&
                localStorage.getItem("jwtToken").length === 172,
            url: props.url
        };
    }
    render() {
        const { url, commentBody, loggedIn, parent, postRef } = this.state;

        return (
            <Form reply>
                <Form.TextArea
                    disabled={!loggedIn}
                    value={commentBody}
                    onChange={e => {
                        this.setState({ commentBody: e.currentTarget.value });
                    }}
                />
                <Button
                    disabled={!loggedIn}
                    content="Post Comment"
                    labelPosition="left"
                    icon="edit"
                    primary
                    onClick={async () => {
                        console.log(commentBody);
                        const r = await fetch(url, {
                            method: "POST",
                            headers: {
                                Authorization:
                                    "Bearer " +
                                    localStorage.getItem("jwtToken"),
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({ body: commentBody })
                        });
                        if (r.ok) {
                            parent.setState({
                                comments: parent.state.comments.concat(
                                    r.comment
                                )
                            });
                            postRef.setState(prevState => ({
                                post: {
                                    ...prevState.post,
                                    comment_count:
                                        postRef.state.post.comment_count
                                }
                            }));
                        } else {
                            console.log(r);
                        }
                    }}
                />
            </Form>
        );
    }
}

export default class CommentList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            post_id: props.post_id,
            postRef: props.parent,
            commentBody: "",
            comments: [],
            url: "http://localhost:5000/post/" + props.post_id + "/comment"
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
        const { comments } = this.state;

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
                <CommentForm
                    parent={this}
                    postRef={this.state.postRef}
                    url={this.state.url}
                />
            </Comment.Group>
        );
    }
}
