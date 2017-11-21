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

class Button extends React.Component {
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
            <button type="button" className="btn btn-primary" onClick={onClick} title={title}/>
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
    }

    next() {

    }

    back() {

    }

    reset() {

    }

    renderButtons() {
        const {
            data,
            page
        } = this.props;
        let buttons = null;
        if(page <= 1) {
            buttons = [ new Button({onClick: this.next, title: "next"}),
            ];
        } else if(data.ladder.players.length < 30) {
            buttons = [
                new Button({onClick: this.reset, title: "page one"}),
                new Button({onClick: this.back, title: "back"}),
            ];
        } else {
            buttons = [
                new Button({onClick: this.next, title: "page one"}),
                new Button({onClick: this.next, title: "back"}),
                new Button({onClick: this.next, title: "next"}),
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
                <h1>US {data.ladder.bracket} Ladder </h1>
                <h4>Last Updated: {new Date(data.ladder.fetchDate).toDateString()}</h4>
                <div className="col">
                    { data.ladder.players.map((player, index) => (
                        <LadderPlayer key={index} {...player} index={(parseInt(page-1)*30)+index} />
                    ))}
                </div>
                <div className="col" id="pages">
                    <div className="row">
                        { this.renderButtons().map((button, i) => (
                                <Button key={i} onClick={button.onClick} title={button.title} />
                            ))
                        }
                    </div>
                </div>
            </div>
        );
    }
}

export default PvPLadder;