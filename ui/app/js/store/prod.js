import history from 'history';
import { createStore, applyMiddleware, compose } from 'redux';
import { routerMiddleware } from 'connected-react-router';
import thunk from 'redux-thunk';
import reducer from '../reducers';

const store = createStore(
    reducer,
    compose(
        applyMiddleware(
            thunk,
            routerMiddleware(history)
        ),
        window.devToolsExtension ? window.devToolsExtension() : f => f
    )
);

export default store;