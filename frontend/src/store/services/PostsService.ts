import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";


export const postsAPI = createApi({
  reducerPath: 'postsApi',
  baseQuery: fetchBaseQuery({baseUrl: `http://${BACKEND_HOST}`}),
  tagTypes: ['Posts'],
  endpoints: (build) => ({
    fetchAllPosts: build.query<string, null>({
        query: () => ('/posts'),
        providesTags: ['Posts']
      }
    ),
  })
})
