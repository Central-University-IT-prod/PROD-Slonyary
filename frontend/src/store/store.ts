import {combineReducers, configureStore} from "@reduxjs/toolkit";
import {reducer as userReducer} from "./slices/userSlice";
import {reducer as themeReducer} from "./slices/themeSlice";
import {reducer as modalReducer} from "./slices/modalSlice";
import {postsAPI} from "./services/PostsService.ts";

const reducer = combineReducers({
  user: userReducer,
  theme: themeReducer,
  modal: modalReducer,
  [postsAPI.reducerPath]: postsAPI.reducer
})

export const store = configureStore({
  reducer,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(postsAPI.middleware)
})

export type RootState = ReturnType<typeof store.getState>