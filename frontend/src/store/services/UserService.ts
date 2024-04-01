import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";
import { IUserModel } from '../../models/UserModels.ts';


export const usersAPI = createApi({
  reducerPath: 'usersApi',
  baseQuery: fetchBaseQuery({baseUrl: BACKEND_HOST, prepareHeaders: (headers) => {
    headers.set('authorization', `Bearer ${localStorage.getItem('accessToken')}`)
  } }),
  tagTypes: ['User'],
  endpoints: (build) => ({
    getUser: build.query<IUserModel[], any>({
        query: () => ({url: `/thisUser`}),
      }
    )
  })
})