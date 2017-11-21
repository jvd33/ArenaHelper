import { InMemoryCache } from 'apollo-cache-inmemory';
import { createHttpLink } from 'apollo-link-http';
import { ApolloClient } from 'apollo-client';

const client = new ApolloClient({
    link: createHttpLink({
        uri: 'http://localhost:4000/graphql',
    }),
    cache: new InMemoryCache({
        dataIdFromObject: o => o.Id,
    }),
    opts: {
      mode: 'no-cors',
    },
});

export default client;