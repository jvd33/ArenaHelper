import React from 'react';
import { Route, Switch } from 'react-router-dom';

import PvPLadders from 'ladder/containers/pvpladders';

const Ladder = () => (
    <div className="container">
        <Switch>
            <Route exact path="/ladder/" component={() =><PvPLadders bracket="2v2" />} />
        </Switch>
    </div>
);

export default Ladder;