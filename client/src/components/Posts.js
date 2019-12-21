import React from "react";
import { List, Header, Image, Card } from "semantic-ui-react";
// import Post from "Post";

export const Posts = ({ posts }) => {
    return (
        <List>
            {posts.map(post => {
                var datetime_difference = Date.now() - new Date(post.posted_on);

                return (
                    <List.Item key={post.id}>
                        {/* <Post post={post} /> */}
                    </List.Item>
                );
            })}
        </List>
    );
};
