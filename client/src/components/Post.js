import React from "react";
import { List, Header, Image, Card } from "semantic-ui-react";

class Post extends React.Component {
    constructor(props) {
        super(props);
        this.state = props.post;
    }

    render() {
        return (
            <Card fluid className="Card">
                <Card.Content>
                    <Card.Header>{state.title}</Card.Header>
                    <Card.Meta>
                        <span className="time">
                            {datetime_difference}
                        </span>
                    </Card.Meta>
                </Card.Content>
                <Image
                    src="http://hdqwalls.com/wallpapers/cat-green-eyes-4k-i8.jpg"
                    wrapped
                    ui={false}
                />
                <Card.Content extra></Card.Content>
            </Card>
            <Header>
                <p className="Post">Posted by {state.author}</p>
            </Header>
            <Image></Image>
        );
    }
}