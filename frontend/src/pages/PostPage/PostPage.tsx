import {Posts} from './Posts/Posts.tsx'
import {postsAPI} from "../../store/services/PostsService.ts";


function PostPage() {
  const {data} = postsAPI.useFetchAllPostsQuery(null)
  console.log(data)
  return <Posts/>
}

export default PostPage
