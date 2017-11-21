import history from 'history';
import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';

export default connectRouter(history) (state => state);