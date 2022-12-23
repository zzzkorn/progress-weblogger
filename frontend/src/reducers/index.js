import { combineReducers } from 'redux';
import messages from "./messages";


const loggerApp = combineReducers({
    messages,
})

export default loggerApp;
