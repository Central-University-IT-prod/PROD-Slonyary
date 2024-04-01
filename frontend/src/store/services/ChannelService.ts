import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";
import { IUserModel } from '../../models/UserModels.ts';

export const channelsAPI = createApi({
  reducerPath: 'usersApi',
  baseQuery: fetchBaseQuery({baseUrl: BACKEND_HOST, prepareHeaders: (headers) => {
    headers.set('authorization', `Bearer ${localStorage.getItem('accessToken')}`)
  } }),
  tagTypes: ['Channel'],
  endpoints: (build) => ({
    getChannel: build.query<IUserModel[], any>({
        query: ({id}) => ({url: `/channels/${id}`}),
      }
    )
  })
})