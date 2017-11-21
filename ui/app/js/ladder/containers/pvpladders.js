import { graphql } from 'react-apollo';
import Ladder from 'ladder/queries/ladders.graphql';
import PvPLadder from 'ladder/components/pvpladder';

export default graphql(Ladder, {
    options: ({ bracket, page }) => ({ variables: { bracket, page } }),
})(PvPLadder);