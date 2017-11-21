import React from 'react';
import { Route, Switch } from 'react-router-dom';
import PvPLadders from "./components/pvpladders";

const Ladder = () => (
    <div className="container">
        <Switch>
            <Route exact path="/ladder/" component={PvPLadders} />
        </Switch>
    </div>
);

export default Ladder;