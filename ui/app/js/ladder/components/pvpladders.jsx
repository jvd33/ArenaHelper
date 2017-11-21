import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import DisplayLadder from 'ladder/containers/pvpladders';

const PvPLadders = () => (
    <div className="pvpladders">
        <ul className="nav nav-pills">
            <li className="active"><a data-toggle="pill" href="/ladder#2v2">2v2</a></li>
            <li><a data-toggle="pill" href="/ladder#3v3">3v3</a></li>
            <li><a data-toggle="pill" href="/ladder#rbg">Rated Battlegrounds</a></li>
        </ul>

        <div className="tab-content">
            <div id="2v2" className="tab-pane active">
                <div className="col">
                    <DisplayLadder key="2v2" bracket="2v2" />
                </div>
            </div>
        </div>
    </div>
);

export default PvPLadders;

