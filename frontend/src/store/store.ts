import { combineReducers, configureStore } from "@reduxjs/toolkit";
import { reducer as userReducer } from "./slices/userSlice";
import { reducer as themeReducer } from "./slices/themeSlice";
import { reducer as modalReducer } from "./slices/modalSlice";

const reducer = combineReducers({
    user: userReducer,
    theme: themeReducer,
    modal: modalReducer
})

export const store = configureStore({
    reducer
})

export type RootState = ReturnType<typeof store.getState>