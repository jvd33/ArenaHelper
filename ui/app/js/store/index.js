import createReducer from 'reducers';

const store = require('./prod').default;

store.asyncReducers = {};

export function injectAsyncReducer(name, asyncReducer) {
    if (!store.asyncReducers[name]) {
        store.asyncReducers[name] = asyncReducer;
        store.replaceReducer(createReducer(store.asyncReducers));
    }
}

export default store;