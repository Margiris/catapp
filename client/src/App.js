import React from "react";
import { BrowserRouter, Route } from "react-router-dom";
import "./App.css";

import TopMenu from "./components/TopMenu";
import PostList from "./components/PostList";
import PostWithComments from "./components/PostWithComments";
import UserList from "./components/UserList";

function App() {
    return (
        <div>
            <TopMenu />
            <BrowserRouter>
                <Route exact path="/" component={PostList} />
                <Route path="/post/:post_id" component={PostWithComments} />
                <Route path="/user/:name" component={UserList} />
            </BrowserRouter>
            <div>
                Icons made by{" "}
                <a
                    href="https://www.flaticon.com/authors/freepik"
                    title="Freepik"
                >
                    Freepik
                </a>{" "}
                from{" "}
                <a href="https://www.flaticon.com/" title="Flaticon">
                    www.flaticon.com
                </a>
            </div>
        </div>
    );
}

export default App;
