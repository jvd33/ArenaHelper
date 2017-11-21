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
    })
}
export default LadderPlayer;