import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";
import {TPostItem} from '../../models/PostsModels.ts';

interface IPostRequest {
  id: number,
  status: string,
  channel_avatars: [
    string
  ],
  publish_time: '2024-04-01T16:43:09.344Z',
  owner_name: string,
  photos: string[],
  html_text: string,
  plain_text: string,
  views: number,
  reactions: number,
  shared: number,
  is_owner: true
}


export const postsAPI = createApi({
  reducerPath: 'postsApi',
  baseQuery: fetchBaseQuery({
    baseUrl: `http://${BACKEND_HOST}`, prepareHeaders: (headers) => {
      headers.set('authorization', `Bearer ${localStorage.getItem('accessToken')}`)
    }
  }),
  tagTypes: ['Posts'],
  endpoints: (build) => ({
    fetchAllPosts: build.query<IPostRequest[], any>({
        query: () => ({url: `/posts`}),
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
