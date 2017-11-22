import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import DisplayLadder from 'ladder/containers/pvpladders';

const PvPLadders = () => (
    <div className="pvpladders">
        <ul className="nav nav-tabs">
            <li className="active"><a data-toggle="tab" href="/ladder#2v2">2v2</a></li>
            <li><a data-toggle="tab" href="/ladder#3v3">3v3</a></li>
            <li><a data-toggle="tab" href="/ladder#rbg">Rated Battlegrounds</a></li>
        </ul>

        <div className="tab-content">
            <div id="2v2" className="tab-pane active">
                <div className="col">
                    <h1>US 2v2 Ladder</h1>
                    <DisplayLadder key="2v2" bracket="2v2" page="1" />
                </div>
            </div>
            <div id="3v3" className="tab-pane">
                <div className="col">
                    <h1>US 3v3 Ladder</h1>
                    <DisplayLadder key="3v3" bracket="3v3" page="1" />
                </div>
            </div>
            <div id="rbg" className="tab-pane">
                <div className="col">
                    <h1>US Rated Battlegrounds Ladder</h1>
                    <DisplayLadder key="rbg" bracket="rbg" page="1" />
                </div>
            </div>
        </div>
    </div>
);

export default PvPLadders;

