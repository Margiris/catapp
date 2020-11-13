import React from "react";
import {
    Modal,
    Button,
    Form,
    Segment,
    Message,
    Label,
    Menu,
} from "semantic-ui-react";

export default class LoginModal extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: "",
            email: "",
            open_login: false,
            open_signup: false,
            loggedIn: false,
            badCredentials: false,
        };
    }

    close_login = () => this.setState({ open_login: false });
    open_login = () => this.setState({ open_login: true });

    close_signup = () => this.setState({ open_signup: false });
    open_signup = () => this.setState({ open_signup: true });

    render() {
        const { open_login, open_signup } = this.state;

        if (
            localStorage.getItem("jwtToken") === null ||
            localStorage.getItem("jwtToken").length !== 172
        ) {
            return (
                <Menu.Menu position="right">
                    <Menu.Item header>
                        <Modal
                            open={open_login}
                            size="mini"
                            onClose={this.close_login}
                            trigger={
                                <Label
                                    as="a"
                                    content="Login"
                                    icon="sign-in"
                                    color="blue"
                                    onClick={this.open_login}
                                />
                            }
                        >
                            <Modal.Header
                                as="h2"
                                style={{ textAlign: "center" }}
                            >
                                <svg
                                    // className="image"
                                    width="40"
                                    height="40"
                                    viewBox="0 0 228.118 228.118"
                                    style={{
                                        // paddingTop: "2px",
                                        // paddingBottom: "2px",
                                        marginRight: "0.5em",
                                        // marginTop: "0",
                                        fill: "black",
                                    }}
                                >
                                    <path
                                        d="M228.118,12.703l-68.674,13.147c-13.634-6.954-29.059-10.88-45.385-10.88c-16.326,0-31.751,3.926-45.385,10.88L0,12.703
	l15.658,83.45c-1.191,6.167-1.822,12.531-1.822,19.04c0,55.263,44.96,100.223,100.223,100.223
	c55.264,0,100.224-44.96,100.224-100.223c0-6.509-0.631-12.873-1.822-19.04L228.118,12.703z M134.029,175.022
	c-7.911,0-15.038-3.259-19.977-8.675c-4.939,5.42-12.059,8.72-19.961,8.72c-14.878,0-26.982-12.362-26.982-27.362h15
	c0,7,5.375,12.362,11.982,12.362c6.606,0,11.981-5.095,11.981-11.701l-0.107-10.694c-8.808-3.291-15.097-11.967-15.097-21.967h15
	c0,5,3.674,8.19,8.19,8.19s8.191-3.19,8.191-8.19h15c0,10-6.288,18.674-15.096,21.966l-0.107,10.651
	c0,6.53,5.375,11.68,11.981,11.68s11.981-5.297,11.981-12.297h15C161.01,162.705,148.907,175.022,134.029,175.022z"
                                    />
                                </svg>
                                Login to CatPic
                            </Modal.Header>
                            <Modal.Content>
                                <Form size="large">
                                    <Segment stacked>
                                        <Message
                                            hidden={!this.state.badCredentials}
                                            negative
                                        >
                                            Wrong username or password
                                        </Message>
                                        <Form.Input
                                            fluid
                                            icon="user"
                                            iconPosition="left"
                                            placeholder="Username"
                                            value={this.state.username}
                                            onChange={(e) => {
                                                this.setState({
                                                    username: e.target.value,
                                                });
                                            }}
                                        />
                                        <Form.Input
                                            fluid
                                            icon="lock"
                                            iconPosition="left"
                                            placeholder="Password"
                                            type="password"
                                            value={this.state.password}
                                            onChange={(e) => {
                                                this.setState({
                                                    password: e.target.value,
                                                });
                                            }}
                                        />

                                        <Button
                                            content="Login"
                                            labelPosition="left"
                                            icon="sign-in"
                                            primary
                                            fluid
                                            size="tiny"
                                            onClick={() => {
                                                const {
                                                    username,
                                                    password,
                                                } = this.state;

                                                fetch(
                                                    process.env
                                                        .REACT_APP_API_URL +
                                                        "/login",
                                                    {
                                                        method: "GET",
                                                        headers: {
                                                            Authorization:
                                                                "Basic " +
                                                                btoa(
                                                                    username +
                                                                        ":" +
                                                                        password
                                                                ),
                                                        },
                                                    }
                                                ).then((r) => {
                                                    if (r.ok) {
                                                        r.json().then((d) => {
                                                            console.log(d);
                                                            localStorage.setItem(
                                                                "jwtToken",
                                                                d.token
                                                            );
                                                            this.setState({
                                                                loggedIn: true,
                                                                badCredentials: false,
                                                            });
                                                            this.close_login();
                                                        });
                                                    } else {
                                                        this.setState({
                                                            badCredentials: true,
                                                        });
                                                    }
                                                });
                                            }}
                                        />
                                    </Segment>
                                </Form>
                            </Modal.Content>
                        </Modal>
                    </Menu.Item>

                    <Menu.Item header>
                        <Modal
                            open={open_signup}
                            size="mini"
                            onClose={this.close_signup}
                            trigger={
                                <Label
                                    as="a"
                                    content="Sign Up"
                                    icon="signup"
                                    // color="blue"
                                    onClick={this.open_signup}
                                />
                            }
                        >
                            <Modal.Header
                                as="h2"
                                style={{ textAlign: "center" }}
                            >
                                <svg
                                    // className="image"
                                    width="40"
                                    height="40"
                                    viewBox="0 0 228.118 228.118"
                                    style={{
                                        // paddingTop: "2px",
                                        // paddingBottom: "2px",
                                        marginRight: "0.5em",
                                        // marginTop: "0",
                                        fill: "black",
                                    }}
                                >
                                    <path
                                        d="M228.118,12.703l-68.674,13.147c-13.634-6.954-29.059-10.88-45.385-10.88c-16.326,0-31.751,3.926-45.385,10.88L0,12.703
	l15.658,83.45c-1.191,6.167-1.822,12.531-1.822,19.04c0,55.263,44.96,100.223,100.223,100.223
	c55.264,0,100.224-44.96,100.224-100.223c0-6.509-0.631-12.873-1.822-19.04L228.118,12.703z M134.029,175.022
	c-7.911,0-15.038-3.259-19.977-8.675c-4.939,5.42-12.059,8.72-19.961,8.72c-14.878,0-26.982-12.362-26.982-27.362h15
	c0,7,5.375,12.362,11.982,12.362c6.606,0,11.981-5.095,11.981-11.701l-0.107-10.694c-8.808-3.291-15.097-11.967-15.097-21.967h15
	c0,5,3.674,8.19,8.19,8.19s8.191-3.19,8.191-8.19h15c0,10-6.288,18.674-15.096,21.966l-0.107,10.651
	c0,6.53,5.375,11.68,11.981,11.68s11.981-5.297,11.981-12.297h15C161.01,162.705,148.907,175.022,134.029,175.022z"
                                    />
                                </svg>
                                Login to CatPic
                            </Modal.Header>
                            <Modal.Content>
                                <Form size="large">
                                    <Segment stacked>
                                        <Message
                                            hidden={!this.state.badCredentials}
                                            negative
                                        >
                                            Email or username already in use
                                        </Message>
                                        <Form.Input
                                            fluid
                                            icon="user"
                                            iconPosition="left"
                                            placeholder="Username"
                                            value={this.state.username}
                                            onChange={(e) => {
                                                this.setState({
                                                    username: e.target.value,
                                                });
                                            }}
                                        />
                                        <Form.Input
                                            fluid
                                            icon="at"
                                            iconPosition="left"
                                            placeholder="someone@example.com"
                                            type="email"
                                            value={this.state.email}
                                            onChange={(e) => {
                                                this.setState({
                                                    email: e.target.value,
                                                });
                                            }}
                                        />
                                        <Form.Input
                                            fluid
                                            icon="lock"
                                            iconPosition="left"
                                            placeholder="Password"
                                            type="password"
                                            value={this.state.password}
                                            onChange={(e) => {
                                                this.setState({
                                                    password: e.target.value,
                                                });
                                            }}
                                        />

                                        <Button
                                            content="Sign Up"
                                            labelPosition="left"
                                            icon="signup"
                                            primary
                                            fluid
                                            size="tiny"
                                            onClick={() => {
                                                const {
                                                    username,
                                                    password,
                                                    email,
                                                } = this.state;

                                                fetch(
                                                    process.env
                                                        .REACT_APP_API_URL +
                                                        "/user",
                                                    {
                                                        method: "POST",
                                                        headers: {
                                                            "Content-Type":
                                                                "application/json",
                                                        },
                                                        body: JSON.stringify({
                                                            name: username,
                                                            email: email,
                                                            password: password,
                                                        }),
                                                    }
                                                ).then((r) => {
                                                    if (r.ok) {
                                                        fetch(
                                                            process.env
                                                                .REACT_APP_API_URL +
                                                                "/login",
                                                            {
                                                                method: "GET",
                                                                headers: {
                                                                    Authorization:
                                                                        "Basic " +
                                                                        btoa(
                                                                            username +
                                                                                ":" +
                                                                                password
                                                                        ),
                                                                },
                                                            }
                                                        ).then((r) => {
                                                            if (r.ok) {
                                                                r.json().then(
                                                                    (d) => {
                                                                        console.log(
                                                                            d
                                                                        );
                                                                        localStorage.setItem(
                                                                            "jwtToken",
                                                                            d.token
                                                                        );
                                                                        this.setState(
                                                                            {
                                                                                loggedIn: true,
                                                                                badCredentials: false,
                                                                            }
                                                                        );
                                                                        this.close_signup();
                                                                    }
                                                                );
                                                            } else {
                                                                this.setState({
                                                                    badCredentials: true,
                                                                });
                                                            }
                                                        });
                                                    }
                                                });
                                            }}
                                        />
                                    </Segment>
                                </Form>
                            </Modal.Content>
                        </Modal>
                    </Menu.Item>
                </Menu.Menu>
            );
        } else {
            return (
                <Menu.Menu position="right">
                    <Menu.Item header>
                        <Label
                            as="a"
                            content="Logout"
                            icon="sign-out"
                            color="red"
                            onClick={async () => {
                                await fetch(
                                    process.env.REACT_APP_API_URL + "/logout",
                                    {
                                        method: "GET",
                                        headers: {
                                            Authorization:
                                                "Bearer " +
                                                localStorage.getItem(
                                                    "jwtToken"
                                                ),
                                        },
                                    }
                                ).then((_) => {
                                    localStorage.setItem("jwtToken", "");
                                });
                                this.setState({ loggedIn: false });
                            }}
                        />
                    </Menu.Item>
                </Menu.Menu>
            );
        }
    }
}
