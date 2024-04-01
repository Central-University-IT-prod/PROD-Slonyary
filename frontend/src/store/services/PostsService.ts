import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";
import { TPostItem } from '../../models/PostsModels.ts';


export const postsAPI = createApi({
  reducerPath: 'postsApi',
  baseQuery: fetchBaseQuery({baseUrl: BACKEND_HOST, prepareHeaders: (headers) => {
    headers.set('authorization', `Bearer ${localStorage.getItem('accessToken')}`)
  } }),
  tagTypes: ['Posts'],
  
  endpoints: (build) => ({
    fetchAllPosts: build.query<TPostItem[], any>({
        query: ({category, limit}) => ({url: `/post?category=${category}&limit=${limit}`}),
      }
    ),
    getPostInfo: build.query<TPostItem, any>({
      query: ({id}) => ({url: `/post/${id}`}),
    }),
    createPost: build.mutation<TPostItem, any>({
      query: (data) => ({
        url: '/post/create',
        metod: 'POST',
        body: data
      })
    }
  )
  })
})
