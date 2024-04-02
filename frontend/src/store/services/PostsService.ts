import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import {BACKEND_HOST} from "../../constants.ts";
import {TPostItem} from '../../models/PostsModels.ts';

export interface IPostRequest {
  id: number,
  status: string,
  channels: any[]
  publish_time: string,
  owner_name: string,
  photos: string[],
  html_text: string,
  plain_text: string,
  views: number,
  reactions: number,
  shared: number,
  is_owner: true,
}

export const postsAPI = createApi({
  reducerPath: 'postsApi',
  baseQuery: fetchBaseQuery({
    baseUrl: `http://${BACKEND_HOST}`, prepareHeaders: (headers) => {
      headers.set('token', localStorage.getItem('accessToken') as string)
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
    createPost: build.mutation({
        query: (data) => ({
          url: '/posts',
          metod: 'POST',
          body: data
        })
      }
    ),
    acceptPost: build.mutation({
        query: (data) => ({
          url: `/posts/${data}/accept`,
          metod: 'POST',
          body: data
        })
      }
    ),
    downgradePost: build.mutation({
        query: (data) => ({
          url: `/posts/${data}/downgrade`,
          metod: 'POST',
          body: data
        })
      }
    )
  })
})
