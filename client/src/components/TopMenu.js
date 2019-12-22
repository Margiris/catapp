import React from "react";
import {
    Icon,
    Image,
    Menu,
    Responsive,
    Sidebar,
    Button,
    Segment,
    Container
} from "semantic-ui-react";

const HeaderMenu = ({ activeItem, handleItemClick }) => (
    <Container>
        <Menu.Item header>
            <Image
                src="/cat.svg"
                height="15px"
                style={{ marginRight: "0.5em" }}
            />
            CatPic
        </Menu.Item>
        <Menu.Item
            name="home"
            active={activeItem === "home"}
            onClick={handleItemClick}
        >
            <Icon name="home" />
            Home
        </Menu.Item>
        <Menu.Item
            name="user"
            active={activeItem === "user"}
            onClick={handleItemClick}
        >
            <Icon name="user" />
            My Profile
        </Menu.Item>
    </Container>
);
//     <Menu icon="labeled" pointing secondary>
//         <Menu.Item header>
//             <span style={{ display: "flex" }}>
//                 <Image
//                     src="cat.svg"
//                     height="15px"
//                     style={{ padding: "0px 4px 0 0" }}
//                 />
//                 CatPic
//             </span>
//         </Menu.Item>
//         <Menu.Item
//             name="home"
//             active={activeItem === "home"}
//             onClick={handleItemClick}
//         >
//             <span>
//                 <Icon name="home" />
//                 Home
//             </span>
//         </Menu.Item>
//         <Menu.Item
//             name="user"
//             active={activeItem === "user"}
//             onClick={handleItemClick}
//         >
//             <span>
//                 <Icon name="user" />
//                 My Profile
//             </span>
//         </Menu.Item>
//         {/* <Menu.Menu position="right">
//     <Menu.Item
//         name="logout"
//         active={activeItem === "logout"}
//         onClick={handleItemClick}
//     />
// </Menu.Menu> */}
//     </Menu>
// );

// const SidebarMenu = ({ activeItem, handleItemClick }) => {
//     return (
//         <Sidebar.Pushable>
//             <Sidebar
//                 as={Menu}
//                 icon="labeled"
//                 pointing
//                 secondary
//                 animation="overlay"
//                 onHide={() => setVisible(false)}
//                 visible={visible}
//                 width="thin"
//             >
//                 <Menu.Item header>
//                     <span style={{ display: "flex" }}>
//                         <Image
//                             src="cat.svg"
//                             height="15px"
//                             style={{ padding: "0px 4px 0 0" }}
//                         />
//                         CatPic
//                     </span>
//                 </Menu.Item>
//                 <Menu.Item
//                     name="home"
//                     active={activeItem === "home"}
//                     onClick={handleItemClick}
//                 >
//                     <span>
//                         <Icon name="home" />
//                         Home
//                     </span>
//                 </Menu.Item>
//                 <Menu.Item
//                     name="user"
//                     active={activeItem === "user"}
//                     onClick={handleItemClick}
//                 >
//                     <span>
//                         <Icon name="user" />
//                         My Profile
//                     </span>
//                 </Menu.Item>
//             </Sidebar>
//             <Sidebar.Pusher></Sidebar.Pusher>
//         </Sidebar.Pushable>
//     );
// };

export default class TopMenu extends React.Component {
    constructor(props) {
        super(props);
        this.state = { activeItem: "home", visible: false };
    }

    handleItemClick = (e, { name }) => this.setState({ activeItem: name });
    setVisible = v => this.setState({ visible: v });

    render() {
        const { activeItem } = this.state;

        return (
            <Menu
                fixed="top"
                pointing
                secondary
                inverted
                stackable
                style={{ backgroundColor: "#1b1c1d" }}
            >
                <Container>
                    <Menu.Item
                        header
                        style={{ paddingTop: "2px", paddingBottom: "2px" }}
                    >
                        <Icon name="bars" className="bars" />
                        <svg
                            width="29"
                            height="29"
                            viewBox="0 0 228.118 228.118"
                            style={{ marginRight: "0.5em" }}
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
                        CatPic
                    </Menu.Item>
                    <Menu.Item
                        name="home"
                        active={activeItem === "home"}
                        onClick={this.handleItemClick}
                    >
                        <Icon name="home" />
                        Home
                    </Menu.Item>
                    <Menu.Item
                        name="user"
                        active={activeItem === "user"}
                        onClick={this.handleItemClick}
                    >
                        <Icon name="user" />
                        My Profile
                    </Menu.Item>
                </Container>
            </Menu>
        );
    }
}
