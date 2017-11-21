import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const LadderPlayer = ({ player }) => (
        <div className="row">
            <div className="col">{player.rank}</div>
            <div className="col">{player.name}-{player.realmName}</div>
            <div className="col">Wins: {player.seasonWins} Losses: {player.seasonLosses}></div>
        </div>

);

LadderPlayer.propTypes = {
    player: PropTypes.shape({
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
    })
}
export default LadderPlayer;