import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const LadderPlayer = ({ rank, rating, name, realmName, raceId, classId,
                          specId, faction, seasonWins, seasonLosses,
                          weeklyWins, weeklyLosses, index }) =>
    (
        <div className="row">
            <div className="col">{index+1}</div>
            <div className="col">{name}-{realmName}</div>
            <div className="col">Wins: {seasonWins} Losses: {seasonLosses}</div>
        </div>

);

LadderPlayer.propTypes = {
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
    index: PropTypes.number,
};
export default LadderPlayer;