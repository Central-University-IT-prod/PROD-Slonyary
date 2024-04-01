import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";

export const channelsAPI = createApi({
  reducerPath: 'usersApi',
  baseQuery: fetchBaseQuery({
    baseUrl: `http://${BACKEND_HOST}`, prepareHeaders: (headers) => {
      headers.set('authorization', `Bearer ${localStorage.getItem('accessToken')}`)
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