import React from "react";
import { Image, Card, Icon } from "semantic-ui-react";
import { NavLink } from "react-router-dom";

class Post extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            post: props.post
        };
        console.log(props);
    }

    render() {
        var datetime_difference =
            Date.now() - new Date(this.state.post.posted_on);

        return (
            <Card fluid className="Card">
                <Card.Content>
                    <Card.Header>
                        <NavLink
                            to={"/post/" + this.state.post.id}
                            className="a"
                        >
                            {this.state.post.title}
                        </NavLink>
                    </Card.Header>
                </Card.Content>
                <Image
                    src="http://hdqwalls.com/wallpapers/cat-green-eyes-4k-i8.jpg"
                    href={"/post/" + this.state.post.id}
                    ui={false}
                />
                <Card.Content>
                    <Card.Meta>
                        <span className="time">
                            <NavLink
                                to={"/user/" + this.state.post.author}
                                className="a"
                            >
                                {this.state.post.author}
                            </NavLink>
                            {" · "}
                            {datetime_difference}
                        </span>
                    </Card.Meta>
                </Card.Content>
                <Card.Content extra>
                    <NavLink to={"/post/" + this.state.post.id}>
                        <Icon name="comments" />
                        {this.state.post.comment_count} comments
                    </NavLink>
                </Card.Content>
            </Card>
        );
    }
}

export default Post;
