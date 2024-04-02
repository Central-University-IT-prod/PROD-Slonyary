import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";

export const channelsAPI = createApi({
  reducerPath: 'usersApi',
  baseQuery: fetchBaseQuery({
    baseUrl: `http://${BACKEND_HOST}`, prepareHeaders: (headers) => {
      headers.set('token', localStorage.getItem('accessToken') as string)
    }
  }),
  tagTypes: ['Channel'],
  endpoints: (build) => ({
    getChannels: build.query({
        query: () => ({url: `/channels/tg`}),
      }
    )
  })
})