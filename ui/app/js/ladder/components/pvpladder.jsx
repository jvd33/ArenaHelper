import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import LadderPlayer from 'ladder/components/player';

const LadderProps = PropTypes.shape({
    bracket: PropTypes.string,
    players: PropTypes.arrayOf(PropTypes.shape({
        rank: PropTypes.string,
        rating: PropTypes.string,
        name: PropTypes.string,
        realmName: PropTypes.string,
        raceId: PropTypes.string,
        classId: PropTypes.string,
        specId: PropTypes.string,
        faction: PropTypes.string,
        seasonWins: PropTypes.string,
        seasonLosses: PropTypes.string,
        weeklyWins: PropTypes.string,
        weeklyLosses: PropTypes.string,
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
                {data.ladder}
            </div>
        );
    }
}

export default PvPLadder;