import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import PvPLadder from 'ladder/components/pvpladder';

const PvPLadders = ({ data: { ladder, loading } }) => (
    <div className="pvpladders">
        <ul className="nav nav-tabs">
            <li className="active"><a data-toggle="pill" href="#2v2">2v2</a></li>
            <li><a data-toggle="pill" href="#3v3">3v3</a></li>
            <li><a data-toggle="pill" href="#rbg">Rated Battlegrounds</a></li>
        </ul>

        <div className="tab-content">
            <div id="2v2" className="tab-pane">
                <h3>US-2v2 Ladders</h3>
                <div className="row">
                    { loading ? null : ladder.map(ladder => (
                        <PvPLadder {...ladder} />
                    ))}
                </div>
            </div>
        </div>
    </div>
);

PvPLadders.propTypes = {
    data: PropTypes.shape({



    })
}
export default PvPLadders;

