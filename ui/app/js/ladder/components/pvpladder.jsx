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
        data: { ladder: {} },
    };

    static initialized = true;

    constructor() {
        super();
    }

    render() {
        const {
            data: { ladder, loading }
        } = this.props;
        return (
            <div className="pvpladder">
                {ladder}
            </div>
        );
    }
}

export default PvPLadder;