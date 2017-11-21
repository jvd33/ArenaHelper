import React, { Component } from 'react';
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

class PvPLadder extends Component {
    static propTypes = {
        data: PropTypes.shape({
            ladder: LadderProps,
            loading: PropTypes.bool,
        }),
    };

    static defaultProps = {
        data: { ladder: {}, loading: true },
    };

    constructor() {
        super();
    }

    render() {
        const {
            data,
        } = this.props;
        if(data.loading) {
            return ( <div>Loading</div> );
        }
        return (
            <div>
                <h1>US {data.ladder.bracket} Ladder </h1>
                <div className="col">
                    { data.ladder.players.map((player, index) => (
                        <LadderPlayer key={index} {...player} index={index} />
                    ))}
                </div>
            </div>
        );
    }
}

export default PvPLadder;