import React from "react";
import { Menu } from "semantic-ui-react";

class TopMenu extends React.Component {
    constructor(props) {
        super(props);
        this.state = { activeItem: "home" };
    }

    handleItemClick = (e, { name }) => this.setState({ activeItem: name });

    render() {
        const { activeItem } = this.state;

        return (
            <div class="sticky">
                <Menu pointing secondary>
                    <Menu.Item header>CatPic</Menu.Item>
                    <Menu.Item
                        name="home"
                        active={activeItem === "home"}
                        onClick={this.handleItemClick}
                    />
                    <Menu.Item
                        name="my profile"
                        active={activeItem === "messages"}
                        onClick={this.handleItemClick}
                    />
                    <Menu.Menu position="right">
                        <Menu.Item
                            name="logout"
                            active={activeItem === "logout"}
                            onClick={this.handleItemClick}
                        />
                    </Menu.Menu>
                </Menu>
            </div>
        );
    }
}

export default TopMenu;
