import { graphql } from 'react-apollo';
import Ladder from 'ladder/queries/ladders.graphql';
import PvPLadder from 'ladder/components/pvpladder';

export default graphql(Ladder, {
    options: ({ bracket }) => ({ variables: { bracket } }),
})(PvPLadder);