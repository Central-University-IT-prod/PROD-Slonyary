import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";
import {TPostItem} from "../../models/PostsModels.ts";


export const postsAPI = createApi({
  reducerPath: 'postsApi',
  baseQuery: fetchBaseQuery({baseUrl: BACKEND_HOST}),
  tagTypes: ['Posts'],
  endpoints: (build) => ({
    fetchAllPosts: build.query<TPostItem[], null>({
        query: () => ('/posts'),
        providesTags: ['Posts']
      }
    )
  })
})
