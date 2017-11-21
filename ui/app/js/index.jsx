import React from 'react';
import store from 'store';
import history from 'history';
import apolloClient from 'apolloClient';
import { ApolloProvider } from 'react-apollo';
import { ConnectedRouter } from 'connected-react-router';
import { Route, Switch, Redirect } from 'react-router-dom';
import { Provider } from 'react-redux';
import 'scss/App.scss';
import Ladder from 'ladder';

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src="/img/logo.svg" className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

const Root = () => (
    <ApolloProvider client={apolloClient}>
        <Provider store={store}>
            <ConnectedRouter history={history}>
                <div>
                    <Switch>
                        <Route exact path="/" component={App} />
                        <Route path="/ladder" component={Ladder} />
                    </Switch>
                </div>
            </ConnectedRouter>
        </Provider>
    </ApolloProvider>
);

export default Root;
