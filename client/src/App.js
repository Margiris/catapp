import React from "react";
import { BrowserRouter, Route } from "react-router-dom";
import "./App.css";

import TopMenu from "./components/TopMenu";
import PostList from "./components/PostList";
import PostWithComments from "./components/PostWithComments";
import UserList from "./components/UserList";
import { Footer } from "./components/Footer";

function App() {
    return (
        <div>
            <BrowserRouter>
                <Route path="/" component={TopMenu} />
                <Route exact path="/" component={PostList} />
                <Route path="/post/:post_id" component={PostWithComments} />
                <Route path="/user/:name" component={UserList} />
            </BrowserRouter>
            <Footer />
        </div>
    );
}

export default App;
