import React from "react";

class Timer extends React.Component {
    constructor(props) {
        super(props);
        this.intervalSeconds = 5;
        this.state = { seconds: 0 };
    }

    tick() {
        this.setState(state => ({
            seconds: state.seconds + this.intervalSeconds
        }));
    }

    componentDidMount() {
        this.interval = setInterval(
            () => this.tick(),
            this.intervalSeconds * 1000
        );
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        return <span>{this.state.seconds}</span>;
    }
}
