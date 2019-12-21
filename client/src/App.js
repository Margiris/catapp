import React, { useEffect, useState } from "react";
import "./App.css";
import { Posts } from "./components/Posts";
import { Container } from "semantic-ui-react";

function App() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetch("/post").then(response =>
            response.json().then(data => {
                setPosts(data.posts);
            })
        );
    }, []);

    console.log(posts);

    return (
        <Container style={{ marginTop: 40 }}>
            <Posts posts={posts} />
        </Container>
    );
}

export default App;
