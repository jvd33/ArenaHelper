import React, { Component} from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import LadderPlayer from 'ladder/components/player';

const LadderProps = PropTypes.shape({
    bracket: PropTypes.string,
    players: PropTypes.arrayOf(PropTypes.shape({
        rank: PropTypes.number,
        rating: PropTypes.number,
        name: PropTypes.string,
        realmName: PropTypes.string,
        raceId: PropTypes.number,
        classId: PropTypes.number,
        specId: PropTypes.number,
        faction: PropTypes.string,
        seasonWins: PropTypes.number,
        seasonLosses: PropTypes.number,
        weeklyWins: PropTypes.number,
        weeklyLosses: PropTypes.number,
    })),
    fetchDate: PropTypes.string,
});

class Button extends Component {
    static propTypes = {
        onClick: PropTypes.func,
        title: PropTypes.string,
    }
    constructor() {
        super();
    }
    render() {
        const { onClick, title } = this.props;
        return (
            <button type="button" className="btn btn-primary" onClick={onClick}>{title}</button>
        );
    }
}

class PvPLadder extends Component {
    static propTypes = {
        data: PropTypes.shape({
            ladder: LadderProps,
            loading: PropTypes.bool,
        }),
        page: PropTypes.string,
    };

    static defaultProps = {
        data: { ladder: {}, loading: true },
        page: "1",
    };

    constructor() {
        super();
        this.currPage = "1";
        this.reset = this.reset.bind(this);
        this.next = this.next.bind(this);
        this.back = this.back.bind(this);
    }

    next() {
        const {
            data,
        } = this.props;
        var newPage = (parseInt(this.currPage) + 1).toString();
        this.currPage = newPage;
        data.refetch({ bracket: data.ladder.bracket, page:newPage});
    }

    back() {
        const {
            data,
        } = this.props;
        var newPage = (parseInt(this.currPage) - 1).toString();
        this.currPage = newPage;
        data.refetch({ bracket: data.ladder.bracket, page:newPage });
    }

    reset() {
        const {
            data,
        } = this.props;
        this.currPage = "1";
        data.refetch({ bracket: data.ladder.bracket, page:"1" });
    }

    renderButtons() {
        const {
            data,
            page
        } = this.props;
        let buttons = null;
        if(parseInt(this.currPage) <= 1) {
            buttons = [ {onClick: this.next, title: "next"},
            ];
        } else if(data.ladder.players.length < 30) {
            buttons = [
                {onClick: this.reset, title: "page one"},
                {onClick: this.back, title: "back"},
            ];
        } else {
            buttons = [
                {onClick: this.reset, title: "page one"},
                {onClick: this.back, title: "back"},
                {onClick: this.next, title: "next"},
            ];
        }

        return buttons;
    }


    render() {
        const {
            data,
            page
        } = this.props;
        if(data.loading) {
            return ( <div>Loading</div> );
        }
        return (
            <div>
                <div className="col">
                    { data.ladder.players.map((player, index) => (
                        <LadderPlayer key={index} {...player} index={(parseInt(this.currPage-1)*30)+index} />
                    ))}
                </div>
                <div className="col" id="pages">
                    <div className="row">
                        { this.renderButtons().map((button, i) => (
                                <Button key={i} {...button} />
                            ))
                        }
                    </div>
                </div>
                <span>Last Updated: {new Date(data.ladder.fetchDate).toDateString()}</span>
            </div>
        );
    }
}

export default PvPLadder;